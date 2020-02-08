import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False
wu_t = [4109,5142,6384,8351]
wu_p = [5504,6669,7653,10241,11893,13362]
hu_t = [4965,6035,7138,8327]
hu_p = [6184,7241,8166,10408,12224,13823]
g_t = [5306,6028,6916,7646]
g_p = [6261,7094,7826,8868,9890,10793]

T = 7
time = []
for i in range(T+1):
    if i <26:
        time.append("2月"+str(i+1)+'日')
    else:
        time.append("3月" + str(i - 25) + '日')
plt.plot(time[0:4],wu_t,color = 'red',label = '武汉-真实',marker = 'o',linewidth=3)
plt.plot(time[0:4],hu_t,color = 'orange',label = '湖北除武汉-真实',marker = 'D',linewidth=3)
plt.plot(time[0:4],g_t,color = 'blue',label = '全国除湖北-真实',marker = 'v',linewidth=3)
plt.plot(time[1:-1],wu_p,color = 'red',label = '武汉-预测',marker = 'o',linewidth=3,ls=":",markerfacecolor='none')
plt.plot(time[1:-1],hu_p,color = 'orange',label = '湖北除武汉-预测',marker = 'D',linewidth=3,ls=":",markerfacecolor='none')
plt.plot(time[1:-1],g_p,color = 'blue',label = '全国除湖北-预测',marker = 'v',linewidth=3,ls=":",markerfacecolor='none')
plt.title("新冠肺炎累计感染病例数预测结果",fontsize=20)
plt.grid()
plt.legend()
plt.xlabel('日期')
plt.ylabel('确诊人数')
plt.show()
