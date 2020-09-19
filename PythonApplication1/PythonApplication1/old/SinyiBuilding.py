#import re

#def SinyiBuilding(str):
#   if(str == None):    
#        return ""    
#    pattern = '<div class="buy-content-basic-cell"><div class="basic-title">主建物</div><div class="basic-value">6.39坪</div></div>'
#    result1 = re.search(pattern,str)
#    return result1[0]


#file_obj = open("C:\\Users\\labc\\Desktop\\履歷.txt","r",encoding ='UTF-8')
#line = file_obj.readline()

#print(line)

#import requests
#import random
#headers = {
#    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'  #本機電腦的識別
#}
#def load_get(http,charset):
#    a = [str((int)(random.random() * 1000)) for i in range(4)]
#    headers = {
#        'User-Agent':'Mozilla/' + str((int)(random.random() * 10)) + '.0 (Windows NT ' + str((int)(random.random() * 10)) + '.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/' + ".".join(a)  #本機電腦的識別
#    }
#    res = requests.get(http, headers=headers)
#    res.encoding = charset
#    return res.text

#def load_post(http,data):
#    print(data)
#    res = requests.post(http,data)
#    return res.text

#def load_post_get(verification_http,http,data):
#    print(data)
#    rs = requests.session()
#    #session對象讓你能夠跨請求保持某些參數。
#    #它也會在同一個session實例發出的所有請求之間保持cookie，期間使用urllib3的connection pooling功能。
#    #所以如果你向同一主機發送多個請求，底層的TCP連接將會被重用，從而帶來顯著的性能提升。
#    res = rs.post(verification_http,data)
#    res = rs.get(http)
#    return res.text
