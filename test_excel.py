import xlwings as xw
import tablero as tbl

wb = xw.Book('test_python.xlsx')
sht1 = wb.sheets['Hoja1']
sht1.range('B2').value = 45