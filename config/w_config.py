'''
武汉地区参数
'''
from .read_data import wi_data,wr_data,R0,r0EG,r0ML
N = 9000000
e = 1.5
# u为自然死亡率
u = 0.007
r0 = R0[0]
# gamma_1为潜伏期治愈率
gamma_1 = 0
# gamma_2为感染者治愈率
gamma_2 = wr_data/wi_data
# print(gamma_2)
# alpha为潜伏期发展为患者的比例
alpha = 0.143
# I_0为感染个体的初始比例
I_0 =wi_data/N
# β为疾病传播概率
beta =r0*(alpha+u)*(u+gamma_2)/alpha
# E_0为潜伏期个体的初始比例
E_0 = I_0*1.5
# R_0为治愈个体的初始比例
R_0 = wr_data/N
# S_0为易感个体的初始比例
S_0 = 1 - I_0 - E_0 - R_0
# T为传播时间
T = 3
c = []
c.append(N)
c.append(round(S_0*N))
c.append(round(wi_data*e))
c.append(wi_data)
c.append(wr_data)
c.append(r0ML[0])
c.append(r0EG[0])
c.append(R0[0])
c.append(alpha)
c.append(beta)
c.append(gamma_2)
c.append(u)