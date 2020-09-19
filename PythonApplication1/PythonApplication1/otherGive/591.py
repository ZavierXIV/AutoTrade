from selenium import webdriver
import openpyxl
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook
import time

#建立爬蟲物件
class Selenium_591 :
	def __init__(self):
		global b
		l , c ,b = self.Input_Information()
		self.File_Init()
		chrome_options = Options()
		chrome_options.add_argument('--incognito')
		chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0')
		global browser
		browser = webdriver.Chrome(chrome_options=chrome_options)		
		browser.get("https://www.591.com.tw/")
		time.sleep(5)
		localation_select = browser.find_element_by_xpath('//*[@id="area-box-body"]/dl['+ str(l) +']/dd[' + str(c) + ']')
		localation_select.click()
		time.sleep(3)
		search_btn = browser.find_element_by_xpath('/html/body/section[1]/div[3]/div/div[2]/div[2]')
		search_btn.click()
		time.sleep(5)

	def Input_Information(self):
		print("1. 台北市")
		print("2. 新北市")
		print("3. 桃園市")
		print("4. 新竹市")
		print("5. 新竹縣")
		print("6. 宜蘭縣")
		print("7. 基隆市")
		print("8. 台中市")
		print("9. 彰化縣")
		print("10.雲林縣")
		print("11.苗栗縣")
		print("12. 南投縣")
		print("13. 高雄市")
		print("14. 台南市")
		print("15. 嘉義市")
		print("16. 嘉義縣")
		print("17. 屏東縣")
		print("18. 台東縣")
		print("19. 花蓮縣")
		print("20. 澎湖縣")
		print("21. 金門縣")
		print("22. 連江縣")
		
		local = 0
		city = 0
		city_num = input("請輸入縣市代碼 :")
		if city_num=='1' or city_num=='2' or city_num=='3' or city_num=='4' or city_num=='5' or city_num=='6' or city_num=='7' :
			local = 1
			city = city_num
		elif city_num=='8' or city_num=='9' or city_num=='10' or city_num=='11' or city_num=='12' :
			local = 2
			city = int(city_num)-7
		elif city_num=='13' or city_num=='14' or city_num=='15' or city_num=='16' or city_num=='17' :
			local = 3
			city = int(city_num)-12
		elif city_num=='18' or city_num=='19' or city_num=='20' or city_num=='21' or city_num=='22' :
			local = 4			
			city = int(city_num)-17
		global page_num
		page = input("請輸入爬取頁數 :") 
		page_num = int(page)
		return local,city,city_num
		
	def StringProcess(self,data):
		return data.split('|')
	
	def page_down(self,n):
		if n > 6 :
			next = browser.find_element_by_xpath('//*[@id="container"]/section[5]/div/div[1]/div[5]/div/a[14]')
			next.click()
		else :
			next = browser.find_element_by_xpath('//*[@id="container"]/section[5]/div/div[1]/div[5]/div/a[' + str(8+n) + ']')
			next.click()
	
	def WebSource(self):
		try :
			for j in range(0,page_num):
				for i in range(1,30):
					title = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']').find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/li[2]/h3/a').text
					data = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/li[2]/p[1]').text
					house_data = self.StringProcess(data)
					addr = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/li[2]/p[2]/em').text
					price = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/div/i').text
					house_master = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/li[2]/p[3]/em[1]').text
					link = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/li[2]/h3/a').get_attribute('href')
					print(title)
					print(house_data[0])
					print(house_data[1])
					print(house_data[2])
					print(addr)
					print(price)
					print(house_master)
					print(link)
					if len(house_data) >= 4:
						print(house_data[3])
						self.SaveFile("591租屋",title,house_data[0],house_data[2],house_data[3],addr,price,house_master,link,house_data[1])
					else:
						self.SaveFile("591租屋",title,house_data[0],house_data[1],house_data[2],addr,price,house_master,link)
					print("====================================")
				self.page_down(j)
				time.sleep(8)
			print('已完成爬蟲!程式即將關閉.....')
			time.sleep(3)
			browser.quit()
		except :
			print('已完成爬蟲!程式即將關閉.....')
			time.sleep(3)
			browser.quit()

	
	def File_Init(self):
		global  excel_file
		global  sheet
		excel_file = Workbook()
		sheet = excel_file.active
		sheet['A1'] = '來源'
		sheet['B1'] = '標題'
		sheet['C1'] = '形式'
		sheet['D1'] = '格局'
		sheet['E1'] = '坪數'
		sheet['F1'] = '樓層'
		sheet['G1'] = '地址'
		sheet['H1'] = '價格(月)'
		sheet['I1'] = '屋主'
		sheet['J1'] = '網址'


	def SaveFile(self,From,title,house_data0,house_data1,house_data2,addr,price,house_master,link,cut='無'):
		print("Saving....")
		sheet.append([From,title,house_data0,cut,house_data1,house_data2,addr,price,house_master,link])
		print("Saved!")
		excel_file.save('591租屋資料_' + str(b) + '.xlsx')

#主程式運行區	
if __name__ == '__main__':

	sb =  Selenium_591()
	sb.WebSource()

