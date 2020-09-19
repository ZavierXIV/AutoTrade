import openpyxl
from openpyxl import Workbook

def File_Init():
		global excel_file
		global sheet
		global Alphabets
		Alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W']
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
		sheet['K1'] = '押金'
		sheet['L1'] = '車位'
		sheet['M1'] = '管理費'
		sheet['N1'] = '最短租期'
		sheet['O1'] = '開伙'
		sheet['P1'] = '養寵物'
		sheet['Q1'] = '性別要求'
		sheet['R1'] = '朝向'
		sheet['S1'] = '可遷入日'
		sheet['T1'] = '法定用途'
		sheet['U1'] = '建物面積'
		sheet['V1'] = '產權登記'
		sheet['W1'] = '身分要求'

def SaveFile(b,headerList=[],contextList={}):
	row = sheet.max_row + 1 
	print(row)
	print("Saving....")
	if len(headerList) > 8 :
		sheet.append(["591",headerList[0],headerList[1],headerList[2],headerList[3],headerList[8],headerList[4],headerList[5],headerList[6],headerList[7]])
	else :
		sheet.append(["591",headerList[0],headerList[1],"無",headerList[2],headerList[3],headerList[4],headerList[5],headerList[6],headerList[7]])
	print("header save ok")
	for data in list(contextList.keys()) :
		for a in Alphabets:
			if sheet[ a +'1'].value == data:
				sheet[a+str(row)]= contextList[data]
				break
	
	for k in Alphabets:
		if sheet[k + str(row)].value == None:
			sheet[k + str(row)] = "無"
	print("Saved!")
	excel_file.save('591租屋資料_' + str(b) + '.xlsx')