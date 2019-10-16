#encoding=utf-8
import pandas as pd
import numpy as np
import xlrd

blank_path = 'D:\\CEKIOSK\\dataframe\\julei\\blanktable.xlsx'
raw1_path='D:\\CEKIOSK\\dataframe\\julei\\finalyu1.xlsx'
raw2_path='D:\\CEKIOSK\\dataframe\\julei\\finalyu2.xlsx'
raw3_path='D:\\CEKIOSK\\dataframe\\julei\\finalyu3.xlsx'
rawl_path='D:\\CEKIOSK\\dataframe\\julei\\finallao.xlsx'

b_table = pd.read_excel(rawl_path, sheetname='blank')
#空表
def get_rawnum(raw1_path):#抽取数据
    yu1_raw = pd.read_excel(raw1_path, sheetname='Sheet1')
    yu1=pd.DataFrame(yu1_raw,columns=['variety','num','day'])
    return yu1

table=b_table.set_index('variety')
#yu1=yu1.set_index('num')
# yu1=get_rawnum(raw1_path)
# yu2=get_rawnum(raw2_path)
# yu3=get_rawnum(raw3_path)

#yu1=pd.concat([yu1,yu2,yu3])
lao = get_rawnum(rawl_path)

print(lao)

# attr = pd.read_excel(rawl_path, sheetname='Sheet1')
# date = attr['date']
# bird= attr.loc[0:62,'bird']
# l_date=list(date)
# l_bird=list(bird)

for i in lao.iterrows():
    print(i[1][0])
    birds=i[1][0]#得到鸟名
    num=i[1][1]#得数量
    days=i[1][2]
#    if days in l_date and birds in l_bird:
    table[days][birds] = num

writer=pd.ExcelWriter('D:\\CEKIOSK\\dataframe\\julei\\newtablelao.xlsx')
table.to_excel(writer,sheet_name='Sheet1')
writer.save()

#    print(yu1['num'][i])

# dt=date[0]
# name =bird[0]
# table[dt][name]=666#是先取列再去行
#
# print(table.ix[0,0])#直接取一个值的办法
#
# #print(b_table)

#判断在不在一个list里面

# theList = ['a','b','c']
# if 'a' in theList and 'b' in theList:
#     print('a in the list')#用来判断要不要采取这个值