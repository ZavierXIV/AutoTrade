from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class Selenium_591 :
	def __init__(self,l,c):
		print(l,c)
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

		
	def StringProcess(self,data):
		return data.split('|')
	
	def page_down(self,n):
		if n > 6 :
			next = browser.find_element_by_xpath('//*[@id="container"]/section[5]/div/div[1]/div[5]/div/a[14]')
			next.click()
		else :
			next = browser.find_element_by_xpath('//*[@id="container"]/section[5]/div/div[1]/div[5]/div/a[' + str(8+n) + ']')
			next.click()
	
	def Header(self,i):
		AllData =[]
		#爬取外觀資訊
		title = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']').find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/li[2]/h3/a').text
		data = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/li[2]/p[1]').text
		house_data = self.StringProcess(data)
		addr = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/li[2]/p[2]/em').text
		price = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/div/i').text
		house_master = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/li[2]/p[3]/em[1]').text
		link = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/li[2]/h3/a').get_attribute('href')
		AllData.append(title)
		AllData.append(house_data[0])
		AllData.append(house_data[1])
		AllData.append(house_data[2])
		AllData.append(addr)
		AllData.append(price)
		AllData.append(house_master)
		AllData.append(link)	
		#print(title)
		#print(house_data[0])
		#print(house_data[1])
		#print(house_data[2])
		#print(addr)
		#print(price)
		#print(house_master)
		#print(link)
		if len(house_data) >= 4:
			#print(house_data[3])
			AllData.append(house_data[3])
		return AllData
	
	def content(self,i):
		Detail = {}
		#進入詳細頁面
		DetailButton = browser.find_element_by_xpath('//*[@id="content"]/ul['+  str(i) +']/li[2]/h3/a')
		DetailButton.click()
		handles = browser.window_handles
		browser.switch_to_window(handles[1])
		time.sleep(5)

		#爬取詳細頁資料
		for m in range(1,15):
			try :
				dt_name = browser.find_element_by_xpath('//*[@id="main"]/div[3]/div[2]/div[1]/ul[1]/li['+  str(m) +']/div[1]').text
				dt = browser.find_element_by_xpath('//*[@id="main"]/div[3]/div[2]/div[1]/ul[1]/li['+ str(m) +']/div[2]/em').text
				Detail[dt_name] = dt
			except:
				break
		"""
		for m in range(len(Detail)):
			print(list(Detail)[m],end = '')
			print(":",end = '')
			print(list(Detail.values())[m])
		"""
		browser.close()
		browser.switch_to_window(handles[0])
		time.sleep(5)
		return Detail

	def Exit(self):
		time.sleep(3)
		browser.quit()