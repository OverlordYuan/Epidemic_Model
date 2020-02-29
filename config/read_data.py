# -*- coding: utf-8 -*-

'''
 Created by Overlord Yuan at 2020/02/08
R0值生成及数据读入程序
'''
from .R_config import R_path
import pandas as pd
import os
from datetime import timedelta, date
import numpy as np
import subprocess

'''运行R程序计算R0值'''
print("----------------------------------------------------")
print("运行R程序")
# R_path = "C:\Program Files\R\R-3.6.2\\bin\\Rscript"
program_path = os.path.join( os.path.abspath(os.path.join(os.getcwd(), ".")),"R/get_update_R0_v5.R")
print(program_path)
path = R_path+" "+program_path
# subprocess.call(path)
subprocess.call([R_path,program_path])
print("R程序运行结束。")
print("----------------------------------------------------")
def get_day_of_day(n=0):
    '''''
    获取时间
    if n>=0,date is larger than today
    if n<0,date is less than today
    date format = "YYYY-MM-DD"
    '''
    if(n<0):
        n = abs(n)
        return date.today()-timedelta(days=n)
    else:
        return date.today()+timedelta(days=n)
time = get_day_of_day(0).strftime("%Y%m%d")

'''获取数据存储路径'''
I_data_path =  os.path.join(os.path.abspath(os.path.join(os.getcwd(), ".")),'data/I_data/2019-nCoV-'+time+'.xlsx')
R0_data_path =  os.path.join(os.path.abspath(os.path.join(os.getcwd(), ".")),'data/R0_data/R0-'+time+'.xlsx')
last_pre_data_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), ".")),'output/预测结果-'+get_day_of_day(-1).strftime("%Y%m%d")+'.xls')
print("读入确诊数据:"+I_data_path)
print("读入R0数据:"+R0_data_path)
print("读入昨天预测数据:"+last_pre_data_path)
'''获取武汉数据'''
w = pd.DataFrame(pd.read_excel(I_data_path,sheet_name='武汉'))
#获取确诊人数
wi_data = w["累计确诊"].tolist()[-1]
wi_data_1= w["累计确诊"].tolist()[-2]
# print("武汉确诊人数："+str(wi_data))
# 获取治愈人数
wr_data = w["累计治愈"].tolist()[-1]
wr_data_1 = w["累计治愈"].tolist()[-2]

'''获取湖北数据'''
h = pd.DataFrame(pd.read_excel(I_data_path,sheet_name='湖北'))
#获取确诊人数
hi_data = h["累计确诊"].tolist()[-1]
# print("湖北确诊人数："+str(hi_data))
# 获取治愈人数
hr_data = h["累计治愈"].tolist()[-1]
# print("湖北治愈人数："+str(hr_data))
hi_data_1 = h["累计确诊"].tolist()[-2]
# print("湖北确诊人数："+str(hi_data))
# 获取治愈人数
hr_data_1 = h["累计治愈"].tolist()[-2]
# 获取疑似人数
hy_data = h["现有疑似"].tolist()[-1]
'''获取全国数据'''
g = pd.DataFrame(pd.read_excel(I_data_path,sheet_name='全国'))
#获取确诊人数
# print(g)
# gi_data = g.iloc[:,1].tolist()[-1]
gi_data = g["累计确诊"].tolist()[-1]
# print("全国确诊人数："+str(gi_data))
# 获取治愈人数
gr_data =g["累计治愈"].tolist()[-1]
# print("全国治愈人数："+str(gr_data))
gi_data_1 = g["累计确诊"].tolist()[-2]
# print("全国确诊人数："+str(gi_data))
# 获取治愈人数
gr_data_1 =g["累计治愈"].tolist()[-2]
# 获取疑似人数
gy_data = g["现有疑似"].tolist()[-1]
'''读取R0数据'''
r0 = pd.DataFrame(pd.read_excel(R0_data_path,sheet_name='R0 ML'))
r0_list= r0.iloc[-1].tolist()[1:]
r0ML=[]
r0ML.append(r0_list[0])
r0ML.append(r0_list[3])
r0ML.append(r0_list[6])
r0 = pd.DataFrame(pd.read_excel(R0_data_path,sheet_name='R0 EG'))
r0_list= r0.iloc[-1].tolist()[1:]
r0EG=[]
r0EG.append(r0_list[0])
r0EG.append(r0_list[3])
r0EG.append(r0_list[6])
R0 =  np.array([r0EG[i]+r0ML[i] for i in range(0,len(r0EG))])/2

'''读取前一天预测数据'''
pre = pd.DataFrame(pd.read_excel(last_pre_data_path,sheet_name='预测结果',index_col=0))
data = pre.iloc[0].tolist()
'''读取预RO数据'''
R0_P = pd.DataFrame(pd.read_excel('data/R0.xlsx',sheet_name="R0"))
