from createAddressDir import *
createAddressDir("C:\\", "testDir")
#import bs4
#file_obj = open("C:\\Users\\labc\\Desktop\\python.txt","w",encoding ='UTF-8')
#htmlFile = open('D:\中華電信電傳\中華電信電傳\臺中市 光特版地政電傳全方位地籍資料查詢系統1.html',encoding ='UTF-8')
#objSoup = bs4.BeautifulSoup(htmlFile,'html.parser')
#objValues = objSoup.select('td .right')
#objTitles = objSoup.select('td .left')

#objStrValues = map(lambda x:x.getText(),objValues)
#objStrTitles = map(lambda x:x.getText(),objTitles)
#objDatas = dict(zip(objStrTitles, objStrValues))

#objResults = dict(filter(lambda x: (x[0] == '縣市' or 
#                                    x[0] == '鄉鎮市區' or
#                                    x[0] == '地段' or
#                                    x[0] == '建號' or 
#                                    x[0] == '建物門牌' or
#                                    x[0] == ''), objDatas.items()))


#for key,value in objResults.items():
#    file_obj.writelines(key)
#    file_obj.writelines('\n')
#    file_obj.writelines(value)
#    file_obj.writelines('\n')

#    dictOfNames = {
#   7 : 'sam',
#   8: 'john',
#   9: 'mathew',
#   10: 'riti',
#   11 : 'aadi',
#   12 : 'sachin'
#}

## Filter dictionary by keeping elements whose keys are divisible by 2
#newDict = dict(filter(lambda elem: elem[0] % 2 == 0, dictOfNames.items()))

#import requests
#import re
#import bs4
##url = "D:\關貿網路版地政資訊e點通\新地政資訊e點通\台北市北投區中山路28之5、28之6號地下二層.html"
##url = "https://www.sinyi.com.tw/buy/house/64026S/?breadcrumb=list"
#headers = ("User-Agent", "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
#htmlResult = requests.get(url)
#print(htmlResult)

#import urllib.request
#import re
#from SinyiBuilding import *
#url = "https://www.sinyi.com.tw/buy/house/64026S/?breadcrumb=list"
#headers = ("User-Agent", "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
#proxy = urllib.request.ProxyHandler({'http:':'proxy.hinet.net:80'})
#opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
#opener.addheaders = [headers]
#data = opener.open(url).read().decode('utf-8')           #Byte Object
#pattern = '<div class="buy-content-basic-cell"><div class="basic-title">主建物</div><div class="basic-value">6.39坪</div></div>'
#result1 = re.search(pattern,data)

##print(result1[0])
##str_data = str(data)
##result = SinyiBuilding(str_data)
#print(result1[0])

#pattern = '<td align="center" bgcolor="#FFFfff" nowrap><b>[0-9]+.[0-9]+</b></td>'

##<div class="buy-content-basic-cell"><div class="basic-title">主建物</div><div class="basic-value">6.39坪</div></div>