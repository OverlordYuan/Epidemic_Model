# -*- coding: utf-8 -*-

'''
 Created by Overlord Yuan at 2020/02/12
预测主程序
'''

'''导入参数及数据'''
from model_wuhnan import RES as wu
from model_hubei import RES as hu
from model_dalu import RES as gu

from model_dalu import NEW as gup
from model_hubei import NEW as hup
from model_wuhnan import NEW as wup

from datetime import timedelta, date
import pandas as pd
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


'''获取预测值'''
pre = []
pre.append(np.rint(wu[:,1]).tolist()[1:])
pre.append(np.rint(hu[:,1]).tolist()[1:])
pre.append(np.rint(gu[:,1]).tolist()[1:])

listb = [[r[col] for r in pre] for col in range(len(pre[0]))]
time = []
for i in range(len(listb)):
    time.append(get_day_of_day(i).strftime("%Y-%m-%d"))
head = ["武汉","湖北除武汉","全国除湖北","全国"]
for i,item in enumerate(listb):
    listb[i].append(sum(item))
data = pd.DataFrame(columns=head,index=time,data=listb)
'''获取预测新增值'''
p_data = [wup,hup,gup]
listc = [[r[col] for r in p_data ] for col in range(len(p_data[0]))]
for i,item in enumerate(listc):
    listc[i].append(sum(item))
p_data_df =  pd.DataFrame(columns=head,index=time,data=listc)
'''获取预测痊愈值'''
rec = []
rec.append(np.rint(wu[:,3]).tolist()[1:])
rec.append(np.rint(hu[:,3]).tolist()[1:])
rec.append(np.rint(gu[:,3]).tolist()[1:])

rec_list = [[r[col] for r in rec] for col in range(len(rec[0]))]
time = []
for i in range(len(rec_list)):
    time.append(get_day_of_day(i).strftime("%Y-%m-%d"))
# head = ["武汉","湖北除武汉","全国除湖北","全国"]
for i,item in enumerate(rec_list):
    rec_list[i].append(sum(item))
rec_data = pd.DataFrame(columns=head,index=time,data=rec_list)
'''数据保存'''
writer = pd.ExcelWriter('output/LongForecast/LongForecast-'+get_day_of_day(0).strftime("%Y%m%d")+'.xls')
data.to_excel(writer,"预测结果")
p_data_df.to_excel(writer,"预测新增")
# rec_data.to_excel(writer,"预测痊愈")
writer.save()






