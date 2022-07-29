from xlrd import *


wb = open_workbook("coords.xls")

def outputArray():
    for s in wb.sheets():
        values = []
        for row in range(s.nrows):
            col_value = []
            for col in range(s.ncols):
                value = (s.cell(row,col).value)
                try: value = str(int(value))
                except: pass
                col_value.append(int(value))
            values.append(col_value)
    return(values)
def outputData():
    #take the final path data of the file, convert into into a string of (longitude, latitude) and output the file with comma deliteted format/csv file     
    pass
