#組合的產品
#尚有幾個問題要處理

import openpyxl
import re
from urllib import request
from fake_useragent import UserAgent
import otherGive.parser
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from otherGive.query_map import QueryMap

import pandas as pd
import os
from openpyxl import Workbook
from IO.excel import *

#將路徑和檔名結合
def MergeFileAndPath(file,mydir):
    if file.endswith(".html"):
        return mydir + file 

#input excl path
# html position   
mydir = 'D:/PythonApplication1/PythonApplication1/python關貿/PythonHtml/' 
outputFile = '關貿輸出2020.xlsx'
inputExcelFile = 'D:/PythonApplication1/PythonApplication1/python關貿/網頁匯整.xlsx'
tradeUrl = 'D:/PythonApplication1/PythonApplication1/python關貿/PythonHtml/台北市北投區中央北路二段29號3樓.html'

list = []

# mock browser
ua = UserAgent()
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument('user-agent='+ua.random)



wb=openpyxl.load_workbook(inputExcelFile)
sheet_ranges = wb['工作表1']

count = 1
address = ''
section = ''
theCity = None
while address != None:
    count = count + 1
    address = sheet_ranges[f'D{count}'].value
    section = sheet_ranges[f'Q{count}'].value
    if address != None:
        address = address.split("市")
        theCity = address[0] + '市'
        theCity = theCity.replace('台', '臺')
        print(theCity)

        address = address[1].split("區")
        theTownship = address[0] + '區'
        print(theTownship)

        temp = re.findall("\d+", section)
        sectioncode = temp[0]

        temp = re.findall("\d+-\d+", section)
        number = temp[0]

        # with webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options) as driver:
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        driver.get(tradeUrl)
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()

        theMap = QueryMap()

        v = theCity
        val = theMap.city(v)

        # 地政專屬內容
        # 城市對照
        element = driver.find_element_by_name('country')
        js = f"""document.getElementsByName('country')[0].innerHTML='<OPTION selected value="{val}">{theCity}</OPTION>';"""
        driver.execute_script(js, element)
        print(element.text)
        print(element)

        js = f"arguments[0].setAttribute('value', '{val}')"
        driver.execute_script(js, element)

        # 區對照
        element = driver.find_element_by_name('township')
        js = f"""document.getElementsByName('township')[0].innerHTML='<OPTION selected value="{val}">{theTownship}</OPTION>';"""
        driver.execute_script(js, element)
        print(element.text)
        print(element)

        v = theTownship

        val = theMap.township(v)

        js = f"arguments[0].setAttribute('value', '{val}')"
        driver.execute_script(js, element)

        #地段選項避免為空
        element = driver.find_element_by_class_name('section')
        js = f"""document.getElementsByClassName('section')[0].innerHTML='<OPTION selected value="nothing">nothing</OPTION>';"""
        driver.execute_script(js, element)

        #地段
        element = driver.find_element_by_name('sectioncode')
        js = f"arguments[0].value = arguments[1]"
        driver.execute_script(js, element, sectioncode)

        #建號
        element = driver.find_element_by_class_name('number')
        js = f"arguments[0].value = arguments[1]"
        driver.execute_script(js, element, number)

        js = f"landQuery()"
        driver.execute_script(js)

        data = pd.read_html(tradeUrl, encoding='utf-8')
        html = (data[0][1]).drop([0,1,2], axis=0)  
        list.append(html.tolist())





#資料集 to excel
sheets = ['標示部','所有權部','權利部']
StuffDataToExcel(list,sheets,outputFile)


#files = os.listdir(mydir)
#fileAddPaths = [MergeFileAndPath(x,mydir) for x in files]
#fileAddPaths = filter(lambda x: x != None,fileAddPaths)
#list = []
#sheets = ['標示部','所有權部','權利部']
##將一個個html轉成資料集
#for item in fileAddPaths:
#    data = pd.read_html(item, encoding='utf-8')
#    html = (data[0][1]).drop([0,1,2], axis=0)  
#    list.append(html.tolist())
##資料集 to excel
#StuffDataToExcel(list,sheets,outputFile)