# pylint: disable=abstract-class-instantiated
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import io
import random
import pandas as pd
import openpyxl
from selenium.webdriver.chrome.options import Options
import json
from fake_useragent import UserAgent

page=1
totalPage=100000
tStart=time.time()#開始時間
prjbrand=[]#房屋品牌
prjID=[]#次序
prjName=[]#案名
prjhref=[]#網址
prjaddr=[]#地址
prjprice=[]#價錢
prjPattern=[]#格局
prjNop=[]#坪數
prjStair=[]#樓層
prjAge=[]#屋齡
prjType=[]#種類
prjIndex=[]#索引
prjStamped=[]#加蓋
prjParking=[]#車位
prjImg=[]#外觀
prjtel=[]#電話
prjComu=[]#社區
prjSN=[]#段建號
prjNol=[]#土地坪數
prjDir=[]#朝向
prjMainBui=[]#主建物
prjAb=[]#附屬建物
prjCp=[]#共有部分
chromeOff=False
#driver = webdriver.Chrome('chromedriver.exe')

#chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
ua = UserAgent()
#開啟json
with open('E:\python\PythonProject\get_proxy\proxy.json' , 'r') as reader:
    jf = json.loads(reader.read())

 

#opts.add_argument("--incognito")
#opts.add_argument('user-agent={uaRan}')
#print(uaRan)

while page<=totalPage:
    
   
    time.sleep(20)
    proxy =jf[random.randint(0,len(jf)-1)]['proxy']    
    #chrome_options.add_argument('--proxy-server=' + proxy)
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('user-agent='+ua.random)
    chrome=webdriver.Chrome('../chromedriver.exe',options=chrome_options)
    chrome.get('https://buy.yungching.com.tw/region/%E5%8F%B0%E5%8C%97%E5%B8%82-%E5%8C%97%E6%8A%95%E5%8D%80_c/?pg='+str(page))
    print(str(page)+'外')
    

#q  = driver.find_element_by_name('q')
#q.send_keys('永慶房屋')
#q.send_keys(Keys.RETURN)
#soup=BeautifulSoup(driver.page_source,'lxml')
#for ele in soup.select('#rso h3 a'):
#    print(ele.text)


#driver.find_element_by_link_text('永慶房屋').click()
#time.sleep(2)  
#driver.find_element_by_link_text('台北市全區').click()
#driver.find_element_by_link_text('台北市').click()
#time.sleep(2) 
#driver.find_element_by_xpath("//input[@index=9]").click()
#driver.find_element_by_class_name('search-text-query').click()

    while page<=totalPage:
        print('未進入if')
        
        if (page)%3==0 and chromeOff==False:#每3頁關掉瀏覽器重開
            #driver.close()
            chromeOff=True
            chrome.close()
            break
        else:
            page+=1
            chromeOff=False
        
        print(str(page)+'內')
        temp1=[]
        temp2=[]
        temp3=[]
        temp4=[]
       
    
    #time.sleep(random.uniform(60,90))
        time.sleep(10)
        soup=BeautifulSoup(chrome.page_source,'html.parser')
        
        
        finalPage= soup.find('a',attrs={'ga_label':'buy_page_last'})
        if finalPage.get('href')!="":
            totalPage=int(finalPage.get('href').split("pg=",1)[1])#總頁數
        #print(totalPage)
        
        a_tags = soup.find_all('a',class_="item-title ga_click_trace")
    #處理案名
    #for tag in a_tags:
    #    for child in tag.children:
    #        if child.string.replace(' ','').replace('\n','') !="":
    #            deal=child.string.replace(' ','').replace('\n','')           
    #            prjName.append(deal)
    #處理網址&房屋品牌&次序&段建號
    
        for url in a_tags:
        
            prjbrand.append('永慶')
            prjID.append('=ROW()-1')
            prjSN.append('')
            prjhref.append("https://buy.yungching.com.tw"+url.get('href'))
        #print(tag.get('href'))
    #處理地址&案名
        for addr in a_tags:
            addr=addr.get('title').split(" ",1)
            prjName.append(addr[0])
            prjaddr.append(addr[1])

        price=soup.find_all('span',class_="price-num")
    #處理價錢
        for pri in price:
            prjprice.append(pri.string)

        pattern=soup.find_all('ul',class_="item-info-detail")
    #處理格局
    #ind=0
    
        for pa in pattern:
            for child in pa.children:
            
            #if (ind+1)%2==0 :     
                if  child.string!=None:        
                    deal=child.string.replace(' ','').replace('\n','')           
                    temp1.append(deal)
                else:
                    temp1.append("")
            #ind=ind+1
    #ind=0
            
        for j in range(int(len(temp1))):
        
            if  (j+1)%19!=0:
                temp2.append(temp1[j].replace(' ','').replace('\n',''))
    
        for j in range(int(len(temp2))):
        
            if j%2!=0:
                temp3.append(temp2[j].replace(' ','').replace('\n',''))
  
        for index in range(len(temp3)):
            if (index+3)%9==0:
                prjPattern.append(temp3[index])
    
    #處理坪數
        for index in range(len(temp3)):
            if (index+4)%9==0:
                prjNop.append(temp3[index].strip('建物坪'))
    #處理樓層
        for index in range(len(temp3)):
            if (index+7)%9==0:
                prjStair.append(temp3[index].strip('樓'))
    #處理屋齡
        for index in range(len(temp3)):
            if (index+8)%9==0:
                prjAge.append(temp3[index].strip('年'))
    #處理種類
        for index in range(len(temp3)):
            if (index+9)%9==0:
                prjType.append(temp3[index])
    #處理索引
        div_tags=soup.find_all('div',class_="item-description")
        for index in div_tags:
            temp4=index.string.split(" ",1)
            prjIndex.append(temp4[0])
    #處理加蓋
        for index in range(len(temp3)):
            if (index+2)%9==0:
                prjStamped.append(temp3[index])
    #處理車位
        for index in range(len(temp3)):
            if (index+1)%9==0:
                if temp3[index].find("含車位")!=-1:#找尋含車位
                    prjParking.append("有")
                else:
                    prjParking.append("沒有")
    #進入每個房子頁面
        a=0
        getIn=chrome.find_elements_by_xpath("//a[@class='item-title ga_click_trace']")
        for index in range(len(getIn)):
            
            getIn[index].click()
            print(a)
            a+=1
            time.sleep(20)#random.uniform(5.1,20) 
            wd=chrome.window_handles#獲取當前所有分頁

            chrome.switch_to.window (wd[1])#切換分頁
            soup=BeautifulSoup(chrome.page_source,'html.parser')#獲取該頁面原始碼
        #time.sleep(random.uniform(30,60))
        #處理外觀
            img=soup.find('img',class_='carousel-main-photo')
            prjImg.append(img.get('src'))
        
        #處理電話
            tel=soup.find('div',class_='m-info-tel')
            for index in tel.children:
                if index.string!=None and index.string!='\n':
                    prjtel.append(index.string)
        #處理社區
            comu=soup.find('a',attrs={'style':'text-decoration: underline;'})
            if comu==None:
                prjComu.append("")           
            else:
                prjComu.append(comu.string)
        #處理土地坪數
            Nol=soup.find_all('li',class_='left') 
            prjNol.append(Nol[1].string.replace('土地坪數：','').replace('坪',""))
        
        #處理朝向
            Dir=soup.find_all('ul',class_='detail-list-lv1')
            findit=False
            for index in Dir[len(Dir)-1].children:
                if index!=None:
                    if str(index.string).find('朝向')!=-1 and findit==False:
                        findit=True
                        prjDir.append(index.string)
                
            if findit==False:
                prjDir.append('')
               
        #處理主建物、附屬建物、共有部分
            BS=soup.find('ul','detail-list-lv2')
        
            MBFind=False
            AbFind=False
            CpFind=False
            if BS!=None:
                for index in BS.children:
                    if index!=None:
                        if str(index.string).find('主建物小計')!=-1 and MBFind==False:#主建物
                            MBFind=True
                            prjMainBui.append(index.string.replace('主建物小計：',"").replace('坪',''))
                        elif str(index.string).find('附屬建物小計')!=-1 and AbFind==False:#附屬建物
                            AbFind=True
                            sp=(index.string.replace('附屬建物小計：',"").replace('坪','')).split(" ",1)
                            prjAb.append(sp[0])
                        elif str(index.string).find('共同使用小計')!=-1 and CpFind==False:#共有部分
                            CpFind=True                  
                            prjCp.append(index.string.replace('共同使用小計：',"").replace('坪',''))
            if MBFind==False:
                prjMainBui.append("")
            if AbFind==False:
                prjAb.append('')
            if CpFind==False:
                prjCp.append('')                                   
        #print(len(BS),prjMainBui,prjAb,prjCp)
        
        
            #time.sleep(random.uniform(30,60))
            chrome.close()
            chrome.switch_to.window (wd[0])#切換回原分頁
    #driver.close()
    #print(driver.page_source)

    
    #getIn[0].click()
        chrome.delete_all_cookies()
        #time.sleep(10)
        chrome.find_element_by_xpath('//a[@ga_label="buy_page_next"]').click()#換頁

print(prjCp)
print(len(prjbrand))#房屋品牌
print(len(prjID))#次序
print(len(prjName))#案名
print(len(prjhref))#網址
print(len(prjaddr))#地址
print(len(prjprice))#價錢
print(len(prjPattern))#格局
print(len(prjNop))#坪數
print(len(prjStair))#樓層
print(len(prjAge))#屋齡
print(len(prjType))#種類
print(len(prjIndex))#索引
print(len(prjStamped))#加蓋
print(len(prjParking))#車位
print(len(prjImg))#外觀
print(len(prjtel))#電話
print(len(prjComu))#社區
print(len(prjSN))#段建號
print(len(prjNol))#土地坪數
print(len(prjDir))#朝向
print(len(prjMainBui))#主建物
print(len(prjAb))#附屬建物
print(len(prjCp))#共有部分

#將List轉成dataframe
trans_df={
    '房屋品牌':prjbrand,
    '次序':prjID,
    '案名':prjName,
    '地址':prjaddr,
    '價格':prjprice,
    '格局':prjPattern,
    '加蓋格局':prjStamped,
    '坪數':prjNop,
    '樓層':prjStair,
    '屋齡':prjAge,
    '索引':prjIndex,
    '種類':prjType,
    '外觀':prjImg,
    '車位':prjParking,
    '網址':prjhref,
    '社區':prjComu,
    '段建號':prjSN,
    '土地坪數':prjNol,
    '朝向':prjDir,
    '電話':prjtel,
    '主建物':prjMainBui,
    '附屬建物':prjAb,
    '共有部分':prjCp       
}

df=pd.DataFrame(data=trans_df)
#開啟Excel
ExcelLen = len(prjName)
df=df.set_index('次序')
wb=openpyxl.load_workbook('E:\\python\\PythonProject\\網頁匯整1.xlsx')


#將資料存入Excel
writer=pd.ExcelWriter('E:\\python\\PythonProject\\try.xlsx',engine="openpyxl")
#没有下面这个语句的话excel表将完全被覆盖
writer.book=wb
wb._active_sheet_index=1#修改作用中的sheet
active_sheet = wb.active

df.to_excel(writer,sheet_name='永慶')
#df.to_excel(writer,sheet_name='永慶')
writer.save()
writer.close()
#df_s1=pandas.DataFrame.from_dict(S1_List)
tEnd=time.time()#結束時間
#fp.write(prjAge)
#fp.close()
#print('prjName',prjName)
#print('prjNop',prjNop)
#print('prjPattern',prjPattern)
#print('prjprice',prjprice)
#print('prjaddr',prjaddr)
#print('prjhref',prjhref)
#print('prjType',prjType)
#print('prjStair',prjStair)
#print('prjAge',prjAge)
#print('prjIndex',prjIndex)
#print(prjImg)
#print("It cost %f sec" % (tEnd - tStart))
