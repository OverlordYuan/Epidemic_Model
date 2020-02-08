import scipy.integrate as spi
import numpy as np
from config.w_config import N,beta,alpha,gamma_1,gamma_2,I_0,E_0,R_0,S_0,T
import matplotlib.pyplot as plt
import pandas as pd
# plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
# plt.rcParams['axes.unicode_minus'] = False
# N = 9000000
# # β为疾病传播概率
# beta =0.041856647
#
# # gamma_1为潜伏期治愈率
# gamma_1 = 0
# # gamma_2为感染者治愈率
# gamma_2 = 0.01241178
# # alpha为潜伏期发展为患者的比例
# alpha = 0.1923
# # I_0为感染个体的初始比例
# I_0 =4109/N
# # E_0为潜伏期个体的初始比例
# E_0 = I_0*0
#
# # R_0为治愈个体的初始比例
# R_0 = gamma_2*I_0
# # S_0为易感个体的初始比例
# S_0 = 1 - I_0 - E_0 - R_0
# # T为传播时间
# T = 12
# INI为初始状态下易感个体比例及感染个体比例
INI = (S_0,I_0,E_0,R_0)
# time = []
# for i in range(T+1):
#     if i <26:
#         time.append("2月"+str(i+4)+'日')
#     else:
#         time.append("3月" + str(i - 25) + '日')

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

T_range = np.arange(0,T + 1)

RES = spi.odeint(funcSI,INI,T_range)*N
# print(RES[:,1])


# plt.plot(RES[:,1]*N,color = 'red',label = '确诊人数',marker = '.')
# print(RES[:,1]*N)
# NEW=[]
# temp = RES[:,1]
# for i,item in enumerate(temp):
#     if i ==0:
#         item = item * N
#         NEW.append(item-3215)
#     else:
#         NEW.append((item-temp[i-1])*N)
# # plt.plot( NEW,color = 'orange',label = '新增人数',marker = '.')
# # plt.title('武汉地区疫情感染人数预测')
# # plt.grid()
# # plt.legend()
# # plt.xlabel('Day')
# # plt.ylabel('Proportion')
# # plt.show()
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(time,RES[:,1]*N,color = 'red',label = '确诊人数',marker = '.')
# # ax.plot(time, Rn, '-', label = 'Rn')
# ax2 = ax.twinx()
# ax2.plot(time,NEW,color = 'orange',label = '新增人数',marker = '.')
# ax.legend(loc=0)
# ax.grid()
# ax.set_ylabel(r"武汉地区预计确诊人数（人）")
# ax2.set_ylabel(r"武汉地区预计新增确诊人数（人）")
# ax.set_xlabel("日期")
# # ax2.set_ylim(0, 100000)
# # ax.set_ylim(0,1000000)
# plt.title('武汉地区(EG)疫情感染人数预测')
# xticks=list(range(0,len(time),5)) # 这里设置的是x轴点的位置
# xlabels=[time[x] for x in xticks] #这里设置X轴上的点对应那个totalseed中的值
# xticks.append(len(time))
# # xlabels.append(time[-1])
# ax.set_xticks(xticks)
# ax.set_xticklabels(xlabels, rotation=5)
# plt.grid()
# ax2.legend(loc=0)
# plt.show()
# plt.savefig('0.png')