import os
import sys
import xlrd
from project import db
from project.models.stock import Stock

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__ + "/../..")))
workbook = xlrd.open_workbook('../../stocks.xlsx')
sheet = workbook.sheet_by_index(0)

for i in range(1, 501):
    data = [sheet.cell_value(i, col) for col in range(sheet.ncols)]
    s = Stock(symbol=data[0],
              name=data[1],
              category=data[3],
              location=data[5])
    db.add(s)
    print 'Added {}'.format(data[1])
print 'Done!'
db.commit()