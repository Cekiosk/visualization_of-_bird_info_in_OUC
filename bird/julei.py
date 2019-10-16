#encoding=utf-8
import pandas as pd
import numpy as np
import xlrd


lao_path='D:\\CEKIOSK\\dataframe\\julei\\newtable.xlsx'
yu_path='D:\\CEKIOSK\\dataframe\\julei\\newtablelao.xlsx'

lao= pd.read_excel(lao_path, sheetname='Sheet1')
yu = pd.read_excel(yu_path, sheetname='Sheet1')

all=pd.merge(lao,yu,how='outer')

writer=pd.ExcelWriter('D:\\CEKIOSK\\dataframe\\julei\\tableall.xlsx')
all.to_excel(writer,sheet_name='Sheet1')
writer.save()
print(all)