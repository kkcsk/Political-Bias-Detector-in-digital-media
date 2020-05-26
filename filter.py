import xlrd 

loc = ("dataset.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
iurl = int(input("Enter the index from excel : "))

url = sheet.cell_value(1, 0)
type = sheet.cell_value(iurl,2)
primarytopic = sheet.cell_value(iurl,3)
secondarytopic = sheet.cell_value(iurl,4)
dv = sheet.cell_value(iurl,5)
rv = sheet.cell_value(iurl,6)
list1=[iurl,url,type,primarytopic,secondarytopic,dv,rv]

