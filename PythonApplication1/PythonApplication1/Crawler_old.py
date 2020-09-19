#有經過提鍊的爬蟲
#標題尚未完成

import pandas as pd
import os
from openpyxl import Workbook
from IO.excel import *
#將路徑和檔名結合
def MergeFileAndPath(file,mydir):
    if file.endswith(".html"):
        return mydir + file 





# html position   
mydir = 'D:/PythonApplication1/PythonApplication1/python關貿/PythonHtml/' 
outputFile = '關貿輸出2020.xlsx'


files = os.listdir(mydir)
fileAddPaths = [MergeFileAndPath(x,mydir) for x in files]
fileAddPaths = filter(lambda x: x != None,fileAddPaths)
list = []
sheets = ['標示部','所有權部','權利部']
#將一個個html轉成資料集
for item in fileAddPaths:
    data = pd.read_html(item, encoding='utf-8')
    html = (data[0][1]).drop([0,1,2], axis=0)  
    list.append(html.tolist())
#資料集 to excel
StuffDataToExcel(list,sheets,outputFile)




