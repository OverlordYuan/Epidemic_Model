# -*- coding: utf-8 -*-

'''
 Created by Overlord Yuan at 2020/02/11
武汉预测程序
'''

import scipy.integrate as spi
import numpy as np
from config.w_config import N,beta,alpha,gamma_1,gamma_2,I_0,E_0,R_0,S_0,T,r0,u
import matplotlib.pyplot as plt
from config.read_data import R0_P
from datetime import timedelta, date
plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False
# INI = (S_0,I_0,E_0,R_0)
R0 = R0_P["武汉"].tolist()
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
    Y = np.zeros(6)
    X = prop
    # 易感个体变化
    Y[0] = -X[5] * X[0]*( X[1]--X[3])
    # 感染个体变化
    Y[1] = alpha * X[2]
    # 潜伏期个体变化
    Y[2] = X[5] * X[0] * X[1] - (alpha + gamma_1) * X[2]
    # 治愈个体变化
    Y[3] = gamma_1 * X[2] + X[4] * X[1]
    return Y
def funcSI_0(prop,_):
    Y = np.zeros(6)
    X = prop
    # 易感个体变化
    Y[0] = -Y[5] * X[0]* X[1]
    # 感染个体变化
    Y[1] = alpha * X[2]
    # 潜伏期个体变化
    Y[2] = Y[5] * X[0] * X[1] - (alpha + gamma_1) * X[2]
    # 治愈个体变化
    Y[3] = gamma_1 * X[2] + X[4] * X[1]
    return Y
def funcSI(prop,_):
    Y = np.zeros(6)
    X = prop
    # 易感个体变化
    Y[0] = -Y[5] * X[0]* X[1]
    # 感染个体变化
    Y[1] = alpha * X[2]
    # 潜伏期个体变化
    Y[2] = Y[5] * X[0] * X[1] - (alpha + gamma_1) * X[2]
    # 治愈个体变化
    Y[3] = gamma_1 * X[2] + X[4] * X[1]
    return Y

for i in range(T):
    T_range = np.arange(0, 2)
    if i == 0:
        INI = (S_0,I_0,E_0,R_0,gamma_2,beta)
        RES =  spi.odeint(funcSI_0,INI,T_range).tolist()
    else:
        beta =R0[i-1]*gamma_2
        INI = (RES[-1][0], RES[-1][1], RES[-1][2], RES[-1][3], RES[-1][3]/RES[-1][1],beta)
        temp = spi.odeint(funcSI_0,INI,T_range).tolist()[-1]
        RES.append(temp)
NEW=[]
time = []
RES = np.array(RES)
print(RES[:,1].tolist())
RES = RES*N
temp = RES[:,1]
for i in range(T+1):
    time.append(get_day_of_day(i).strftime("%m-%d"))
    if(i==0):
        continue
    else:
        NEW.append(round((temp[i]-temp[i-1])))

fig = plt.figure()
ax = fig.add_subplot(111)
aa = RES[:,1].tolist()
ax.plot(time[1:],aa[1:],color = 'red',label = '确诊人数',marker = '.')
# plt.ylim(0,42000)
# ax.plot(time, Rn, '-', label = 'Rn')
ax2 = ax.twinx()
ax2.plot(time[1:],NEW,color = 'orange',label = '新增人数',marker = '.')
# plt.ylim(0,850)
ax.legend(loc=5,bbox_to_anchor=(1,0.25))
ax2.legend(loc=5,bbox_to_anchor=(1,0.15))
ax.grid()
ax.set_ylabel(r"武汉地区预计确诊人数（人）")
ax2.set_ylabel(r"武汉地区预计新增确诊人数（人）")
ax.set_xlabel("日期")

plt.title('武汉地区确诊人数预测')
xticks=list(range(0,len(time),5),) # 这里设置的是x轴点的位置
xlabels=[time[x] for x in xticks] #这里设置X轴上的点对应那个totalseed中的值
xticks.append(len(time))
# xlabels.append(time[-1])
ax.set_xticks(xticks)
ax.set_xticklabels(xlabels, rotation=30)
plt.grid()

# plt.get_current_fig_manager().window.state('zoomed')
plt.savefig('picture/武汉地区疫情感染人数预测'+get_day_of_day(0).strftime("%m-%d")+'.png',bbox_inches='tight',dpi = fig.dpi)
# plt.show()
# plt.close()
# # plt.savefig('picture/武汉地区疫情感染人数预测'+get_day_of_day(0).strftime("%m-%d")+'.png')
