# -*- coding: utf-8 -*-

'''
 Created by Overlord Yuan at 2020/02/12
预测主程序
'''
from model_wuhnan import RES as wu
from model_hubei import RES as hu
from model_dalu import RES as gu

from model_dalu import NEW as gup
from model_hubei import NEW as hup
from model_wuhnan import NEW as wup
from model_wuhnan import time
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta, date
plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False
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
pre.append((np.rint(wu[:,1])+np.rint(hu[:,1])+np.rint(gu[:,1])).tolist()[1:])

'''获取预测新增值'''
p_data = [wup,hup,gup,(np.array(wup)+np.array(hup)+np.array(gup)).tolist()]
# listc = [[r[col] for r in p_data ] for col in range(len(p_data[0]))]

fig = plt.figure()
ax = fig.add_subplot(111)
print(pre[3])
ax.plot(time[1:],pre[-1],color = 'red',label = '确诊人数',marker = '.')
plt.ylim(0,78000)
# ax.plot(time, Rn, '-', label = 'Rn')
ax2 = ax.twinx()
ax2.plot(time[1:],p_data[-1],color = 'orange',label = '新增人数',marker = '.')
ax.legend(loc=5,bbox_to_anchor=(1,0.25))
ax2.legend(loc=5,bbox_to_anchor=(1,0.15))
ax.grid()
ax.set_ylabel(r"全国预计确诊人数（人）")
ax2.set_ylabel(r"全国预计新增确诊人数（人）")
ax.set_xlabel("日期")

plt.title('全国确诊人数预测')
plt.gcf().autofmt_xdate()
xticks=list(range(0,len(time),5)) # 这里设置的是x轴点的位置
xlabels=[time[x] for x in xticks] #这里设置X轴上的点对应那个totalseed中的值
xticks.append(len(time))
# xlabels.append(time[-1])
ax.set_xticks(xticks)
ax.set_xticklabels(xlabels, rotation=30)
plt.grid()
plt.savefig('picture/全国疫情感染人数预测'+get_day_of_day(0).strftime("%m-%d")+'.png',bbox_inches='tight',dpi = fig.dpi)