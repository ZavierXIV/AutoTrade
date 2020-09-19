from CityNumber import *
from SeleniumWeb import *
from excel import *
from YungData import *
	
#主程式運行區	
if __name__ == '__main__':
	global page_num
	global b
	global houses
	houses = GetHouse()
	l,c,b,page_num = Input_Information()
	sb =  Selenium_591(l,c)
	try :
		for j in range(0,page_num):
			for i in range(1,30):
				sb.Header(i)
				sb.content(i)
				house = sb.dataBack()
				for a in houses.keys() :
					houses[a].append(house[a][0])
			sb.page_down(j)
		StuffATableToExcel(houses,"591","細抓1.xlsx")
		print('已完成爬蟲!程式即將關閉.....')
		sb.Exit()

	except :
		print('已完成爬蟲!程式即將關閉.....')
		sb.Exit()

