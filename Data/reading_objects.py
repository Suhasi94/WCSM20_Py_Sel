# 1. excel sheet is called as workbook
#2. once you open u should get the handle
#3. get the data from the rows present in the sheet and interact with its cells
### pip install xlrd==1.2.0


import xlrd
path = r"C:\Users\User\OneDrive\Desktop\file_data.xlsx"


def read_locators():
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name("loginpage")
    rows = worksheet.get_rows() # it creates a generator object
    print(rows)
    header = next(rows)
    d = {}
    for row in rows:
        d[row[0].value] = (row[1].value,row[2].value)
        #print(row[0].value,row[1].value,row[2].value)
    return d

#print(read_locators())
"""

def read_locators():
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name("loginpage")
    rows = worksheet.nrows
    print(rows)
    d = {}
    for i in range(1,rows):
        row = worksheet.row_values(i)
        d[row[0]] = (row[1],row[2])
    return d


print(read_locators())

"""