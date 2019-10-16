#encoding=utf-8
import pandas as pd
import numpy as np
import xlrd


raw_path='D:\\CEKIOSK\\dataframe\\juleidraw\\mulu.xlsx'
write_path='D:\\CEKIOSK\\dataframe\\juleidraw\\allmulu.xlsx'

mulu1= pd.read_excel(raw_path, sheetname='mu')
mulu2 = pd.read_excel(write_path, sheetname='all3')

all=pd.merge(mulu1,mulu2,how='right')

writer=pd.ExcelWriter(write_path)
all.to_excel(writer,sheet_name='all4')
writer.save()
print(all)