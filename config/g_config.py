# -*- coding: utf-8 -*-

'''
 Created by Overlord Yuan at 2020/02/08
全国除湖北参数设置
'''
from .read_data import gi_data,gr_data,hi_data,hr_data,R0,r0EG,r0ML,gy_data,hy_data
from .e_config import g_e,T
#e为潜伏期人数/实际确证人数
e = g_e
# N为总人口数
N = 1300000000
# u为自然死亡率
u = 0.007
r0 = R0[2]
# r0 = 0.5
# gamma_1为潜伏期治愈率

# gamma_2为感染者治愈率
gamma_2 = (gr_data-hr_data)/(gi_data-hi_data)
gamma_1 = gamma_2/2
# print(gamma_2)
# alpha为潜伏期发展为患者的比例
alpha = 0.02
# I_0为感染个体的初始比例
I_0 =(gi_data-hi_data)/N
# β为疾病传播概率
beta =r0*(alpha+u)*(u+gamma_2)/alpha
# E_0为潜伏期个体的初始比例
E_0 = (gy_data-hy_data)/N
# R_0为治愈个体的初始比例
R_0 = (gr_data-hr_data)/N
# S_0为易感个体的初始比例
S_0 = 1 - I_0 - E_0 - R_0
# T为传播时间
# T = 30

'''参数汇总'''
c = []
c.append(N)
c.append(round(S_0*N))
c.append(round(gy_data-hy_data))
c.append(gi_data-hi_data)
c.append(gr_data-hr_data)
c.append(r0ML[2])
c.append(r0EG[2])
c.append(R0[2])
c.append(alpha)
c.append(beta)
c.append(gamma_2)
c.append(u)