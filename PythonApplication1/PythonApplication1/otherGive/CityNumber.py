def Input_Information():
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
	return local,city,city_num,page_num