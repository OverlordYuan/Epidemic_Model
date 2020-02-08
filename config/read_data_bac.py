import pandas as pd
'''
获取武汉数据
'''
from datetime import timedelta, date
import numpy as np

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
time = get_day_of_day(0).strftime("%Y%m%d")
w = pd.DataFrame(pd.read_excel('D:\程序\Epidemic_Model\data/每日数据更新-'+time+'.xlsx',sheet_name='武汉'))
#获取确诊人数
wi_data = w["累计确诊"].tolist()[-1]
wi_data_1= w["累计确诊"].tolist()[-2]
# print("武汉确诊人数："+str(wi_data))
# 获取治愈人数
wr_data = w["累计治愈"].tolist()[-1]
wr_data_1 = w["累计治愈"].tolist()[-2]
# print("武汉治愈人数："+str(wr_data))
'''
获取湖北数据
'''
h = pd.DataFrame(pd.read_excel('D:\程序\Epidemic_Model\data/每日数据更新-'+time+'.xlsx',sheet_name='湖北'))
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

'''
获取全国数据
'''
g = pd.DataFrame(pd.read_excel('D:\程序\Epidemic_Model\data/每日数据更新-'+time+'.xlsx',sheet_name='全国'))
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

'''
读取R0数据
'''
r0 = pd.DataFrame(pd.read_excel('D:\程序\Epidemic_Model\data/每日R0更新-'+time+'.xlsx',sheet_name='R0-ML'))
r0ML= r0.iloc[-1].tolist()[1:]
# r0ML=[]
# r0ML.append(r0_list[0])
# r0ML.append(r0_list[3])
# r0ML.append(r0_list[6])
r0 = pd.DataFrame(pd.read_excel('D:\程序\Epidemic_Model\data/R0-'+time+'.xlsx',sheet_name='R-EG'))
r0EG= r0.iloc[-1].tolist()[1:]
# r0EG=[]
# r0EG.append(r0_list[0])
# r0EG.append(r0_list[3])
# r0EG.append(r0_list[6])
R0 =  np.array([r0EG[i]+r0ML[i] for i in range(0,len(r0EG))])/2
'''
读取前一天预测数据
'''
pre = pd.DataFrame(pd.read_excel('D:\程序\Epidemic_Model\output/预测结果-'+get_day_of_day(-1).strftime("%Y%m%d")+'.xls',sheet_name='预测结果'))
data = pre.iloc[0].tolist()[1:]