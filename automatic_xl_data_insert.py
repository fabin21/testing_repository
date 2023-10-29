
import openpyxl
import pyautogui

# pip install mouseinfo
# mouseinfo.mouseInfo()

filedir = str("")
sheetpagename = str("")
collumns_nametuple = tuple()
collumns_namelist= list(collumns_nametuple)
x_pixel = dict(collumns_namelist, x_coordinatelist)
y_pixel = dict(collumns_namelist, y_coordinatelist)
timeclicklag = float()

workbook = openpyxl.load_workbook(filedir)
sheetpage = workbook[sheetpagename]

for row in sheetpage.iter_rows():
    for i in range(1, len(collumns_nametuple)+1, 1):
        pyautogui.click(
            x_pixel[collumns_nametuple(i)], 
            y_pixel[collumns_nametuple(i)], 
            duration = timeclicklag
        )
        pyautogui.write(str(row[i].value))
