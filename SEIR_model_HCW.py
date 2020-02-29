# -*- coding: utf-8 -*-

'''
 Created by Overlord Yuan at 2020/02/08
湖北除武汉预测程序
'''
import scipy.integrate as spi
import numpy as np
from config.h_config import N,beta,alpha,gamma_1,gamma_2,I_0,E_0,R_0,S_0,T,r0,u
import matplotlib.pyplot as plt
from datetime import timedelta, date
plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False
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
def funcSI(prop,_):
    Y = np.zeros(4)
    X = prop
    # 易感个体变化
    Y[0] = - beta * X[0] * X[1]
    # 感染个体变化
    Y[1] = alpha * X[2] - gamma_2 * X[1]
    # 潜伏期个体变化
    Y[2] = beta * X[0] * X[1] - (alpha + gamma_1) * X[2]
    # 治愈个体变化
    Y[3] = gamma_1 * X[2] + gamma_2 * X[1]
    return Y
T_range = np.arange(0,T+1)
INI = (S_0,I_0,E_0,R_0)
RES = spi.odeint(funcSI,INI,T_range)*N
# NEW=[]
# time = []
# temp = RES[:,1]
# for i in range(T+1):
#     time.append(get_day_of_day(i-1).strftime("%m-%d"))
#     if(i==0):
#         continue
#         # NEW.append(round(temp[i] * N - data[0]))
#     else:
#         NEW.append(round((temp[i]-temp[i-1])))
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(time,RES[:,1]*N,color = 'red',label = '确诊人数',marker = '.')
# # ax.plot(time, Rn, '-', label = 'Rn')
# ax2 = ax.twinx()
# ax2.plot(time[1:],NEW,color = 'orange',label = '新增人数',marker = '.')
# ax.legend(loc=0)
# ax.grid()
# ax.set_ylabel(r"湖北（除）地区预计确诊人数（人）")
# ax2.set_ylabel(r"湖北（除）地区预计新增确诊人数（人）")
# ax.set_xlabel("日期")
#
# plt.title('湖北（除）地区疫情感染人数预测')
# xticks=list(range(0,len(time),5)) # 这里设置的是x轴点的位置
# xlabels=[time[x] for x in xticks] #这里设置X轴上的点对应那个totalseed中的值
# xticks.append(len(time))
# xlabels.append(time[-1])
# ax.set_xticks(xticks)
# ax.set_xticklabels(xlabels, rotation=5)
# plt.grid()
# ax2.legend(loc=0)
# plt.show()