# -*- coding: utf-8 -*-

'''
 Created by Overlord Yuan at 2020/02/08
预测主程序
'''

'''导入参数及数据'''
from model_wuhnan import RES as wu
from model_hubei import RES as hu
from model_dalu import RES as gu
from config.w_config import c as wc
from  config.h_config import c as hc
from config.g_config import c as gc
from datetime import timedelta, date
from  config.read_data import wi_data,hi_data,gi_data,data
from  config.read_data import wi_data_1,hi_data_1,gi_data_1
import pandas as pd
import numpy as np
import xlwt,xlrd
from xlutils.copy import copy
def get_day_of_day(n=0):
    '''''
    if n>=0,date is larger than today
    if n<0,date is less than today
    date format = "YYYY-MM-DD"
    '''
    if(n<0):
        n = abs(n)
        return date.today()-timedelta(days=n)
    else:
        return date.today()+timedelta(days=n)


'''获取前一天预测值'''
last_data = data

'''获取未来三天预测值'''
pre = []
pre.append(np.rint(wu[:,1]).tolist()[1:4])
pre.append(np.rint(hu[:,1]).tolist()[1:4])
pre.append(np.rint(gu[:,1]).tolist()[1:4])

listb = [[r[col] for r in pre] for col in range(len(pre[0]))]
time = []
for i in range(len(listb)):
    time.append(get_day_of_day(i).strftime("%d/%m/%y"))
# time = [get_day_of_day(0).strftime("%d/%m/%y"),get_day_of_day(1).strftime("%d/%m/%y"),get_day_of_day(2).strftime("%d/%m/%y")]
head = ["武汉","湖北除武汉","全国除湖北","全国"]
for i,item in enumerate(listb):
    listb[i].append(sum(item))
data = pd.DataFrame(columns=head,index=time,data=listb)

'''生成预测参数'''
index_c = ["武汉","湖北除武汉","全国除湖北"]
head_c = ["N(地区总人口数)","S(健康者人数)","E(潜伏期人数)","I(确诊者人数)","R(痊愈人数)","R0_ML(基本传染数(ML))","R0_EG(基本传染数(EG))","R0_AVERAGE(均值)","alpha(潜伏期转换为感染者的概率)","beta(感染概率)","gama(感染痊愈概率)","u(自然死亡率)"]
c =[wc,hc,gc]
data_c = pd.DataFrame(columns=head_c,index=index_c,data=c)

'''
生成回顾数据
'''
index_0 = ["真实值","预测值","偏差","真实新增","预测新增"]
index_1 = [get_day_of_day(0).strftime("%d/%m/%y"),"预测新增",get_day_of_day(1).strftime("%d/%m/%y"),"预测新增",get_day_of_day(2).strftime("%d/%m/%y"),"预测新增"]
#前2天真实值f
real_data_1 = [wi_data_1,hi_data_1-wi_data_1,gi_data_1-hi_data_1,gi_data_1]
#前1天真实值
real_data = [wi_data,hi_data-wi_data,gi_data-hi_data,gi_data]
# print(last_data)
Rate = list(map(lambda z:str(round(z*100,2))+ '%' if z<0 else "+"+str(round(z*100,2))+ '%',list(map(lambda x, y: x / y,  (np.array(last_data) - np.array(real_data)).tolist(),real_data))))
data_hugu0 = pd.DataFrame(columns=head,index=index_0,data=[real_data,last_data,Rate,(np.array(real_data) - np.array(real_data_1)).tolist(),(np.array(last_data) - np.array(real_data_1)).tolist()])

da = [listb[0],(np.array(listb[0]) - np.array(real_data)).tolist(),listb[1],(np.array(listb[1]) - np.array(listb[0])).tolist(),listb[2],(np.array(listb[2]) - np.array(listb[1])).tolist()]
data_hugu1 =  pd.DataFrame(columns=head,index=index_1,data=da)

'''数据保存'''
writer = pd.ExcelWriter('output/预测结果-'+get_day_of_day(0).strftime("%Y%m%d")+'.xls')
data.to_excel(writer,"预测结果")
data_c.to_excel(writer,"预测参数")
data_hugu0.to_excel(writer,"预测回顾",startcol=0, startrow=1)
data_hugu1.to_excel(writer,"预测回顾",startcol=0, startrow=9)
writer.save()

'''设置预测回顾sheet中的表头'''
save_path = 'output/预测结果-'+get_day_of_day(0).strftime("%Y%m%d")+'.xls'
workbook = xlrd.open_workbook(save_path)  # 打开工作簿
worksheet = workbook.sheet_by_name("预测回顾")  # 获取工作簿中所有表格中的的第一个表格
rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
new_worksheet = new_workbook.get_sheet("预测回顾")  # 获取转化后工作簿中的第一个表格
alignment = xlwt.Alignment() # Create Alignment  创建对齐
alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: 标准化：HORZ_GENERAL, 左对齐：HORZ_LEFT, 水平对齐居中：HORZ_CENTER, 右对齐：HORZ_RIGHT, 填充：HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_CENTER # May be: 顶部对齐：VERT_TOP, 垂直居中：VERT_CENTER, 底部对齐：VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
style = xlwt.XFStyle() # Create Style 创建样式
style.alignment = alignment # Add Alignment to Style  为样式添加对齐
new_worksheet.write_merge(0, 0, 0, 4, get_day_of_day(-1).strftime("%Y-%m-%d")+'预测回顾',style)
new_worksheet.write_merge(8, 8, 0, 4, "未来三天预测结果",style)
# new_worksheet.write(4, 5, "note：百分比形式，正数和负数前加+／-")
new_workbook.save(save_path)
print("保存预测数据:"+save_path)
print("预测数据保存成功！！")





