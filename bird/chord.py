#numpy数组格式都必须是同一种
#encoding=utf-8
import pandas as pd
import numpy as np
import xlrd

#  - 副本
#读调查表→getframe1→读保存文件→getframe2→结合两者→存入保存文件
raw_path='D:\\CEKIOSK\\dataframe\\chord\\chord.xlsx'

xgd = pd.read_excel(raw_path, sheetname='Sheet1', header=None)
print(xgd[0][0])

#for i in range(0,74):
 #   xgd[i][i]=0

for i in range(0,74):
     for j in range(0,74):
        # if(abs(xgd[i][j])<=0.015):
             xgd[i][j]=abs(xgd[i][j])


# for i in xgd.iterrows():
#     print(i[1][0])
    #birds=i[1][0]#得到鸟名
    #num=i[1][1]#得数量
#     days=i[1][2]
# #    if days in l_date and birds in l_bird:
#     table[days][birds] = num
#
writer=pd.ExcelWriter('D:\\CEKIOSK\\dataframe\\chord\\chordabs.xlsx')
xgd.to_excel(writer,sheet_name='Sheet1')
writer.save()


