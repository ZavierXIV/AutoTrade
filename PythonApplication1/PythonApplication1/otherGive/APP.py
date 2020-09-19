from CityNumber import *
from FileProcess import *
from SeleniumWeb import *
	
#主程式運行區	
if __name__ == '__main__':
	global page_num
	global b
	l,c,b,page_num = Input_Information()
	sb =  Selenium_591(l,c)
	File_Init()
	try :
		for j in range(0,page_num):
			for i in range(1,30):
				headerData = sb.Header(i)
				contentData = sb.content(i)
				SaveFile(b,headerData,contentData)
			sb.page_down(j)
		print('已完成爬蟲!程式即將關閉.....')
		sb.Exit()	
	except :
		print('已完成爬蟲!程式即將關閉.....')
		sb.Exit()


