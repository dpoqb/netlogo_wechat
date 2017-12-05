from people.FileRead import FileRead_fmg
import matplotlib.pyplot as plt

_Ni_1_start = [4063,3465,3507,3408,2875,3602,2649,3017,2936,2733]
_Ni_1_stable = [5240,8580,7770,10260,7150,7100,5920,6200,4970,5590]
between_time, speed_change_in_fear_1= [],[]
# 寻找test5-Ru-Ni-1文件下的.csv文件
file_dir="/var/www/html/GitHub/repository/网络反恐Netlogo仿真模型/网络反恐仿真模型/网络反恐仿真实验室/people/test5-Ru-Ni-1"
find_str_1 = "\"average fear index\""
find_str_2 = "\"person public influence\""
find_str_3 = "\"fear-sacle of people\""
Ru = [round(a*0.1,1) for a in range(1,11)]
_avg_fear_index_vs_RuNi_1=FileRead_fmg(file_dir,Ru,[],find_str_1,find_str_2,find_str_3)
_avg_fear_index_vs_RuNi_1.file_name()
_avg_fear_index_vs_RuNi_1.fileSorted()
_avg_fear_index_vs_RuNi_1.getAvgFear()

for i,v in enumerate(_Ni_1_start):
    between_time.append(_Ni_1_stable[i]-v)
_avg_fear_index_vs_RuNi_1.peopel_result_avg_fear_index[-2] = 37.72626262626262
between_time[-2] = 3018
between_time[3] = 4265
for index in range(len(_avg_fear_index_vs_RuNi_1.peopel_result_avg_fear_index)):
#     # 对象列表获取元素--()
    speed_change_in_fear_1.append(round(((float)(_avg_fear_index_vs_RuNi_1.getOneAvgFear(index))-50.00)*1E3/between_time[index],2))
    # print(round(((float)(_avg_fear_index_vs_RuNi_1.getOneAvgFear(index)) - 50.00) * 1E4 / between_time[index], 2))
# print(type(_avg_fear_index_vs_RuNi_1.getOneAvgFear(1)))返回的是一个字符类型
print(speed_change_in_fear_1)

_Ni_10_start = [2482,1798,3425,3021,2823,2146,4430,3187,3399,2325]
_Ni_10_stable = [6220,3780,5220,4560,6850,5730,5740,4490,4380,4340]
between_time, speed_change_in_fear_2= [],[]
# 寻找test5-Ru-Ni-1文件下的.csv文件
file_dir="/var/www/html/GitHub/repository/网络反恐Netlogo仿真模型/网络反恐仿真模型/网络反恐仿真实验室/people/test10-Ru-Ni-10"
find_str_1 = "\"average fear index\""
find_str_2 = "\"person public influence\""
find_str_3 = "\"fear-sacle of people\""
Ru = [round(a*0.1,1) for a in range(1,11)]
_avg_fear_index_vs_RuNi_10=FileRead_fmg(file_dir,Ru,[],find_str_1,find_str_2,find_str_3)
_avg_fear_index_vs_RuNi_10.file_name()
_avg_fear_index_vs_RuNi_10.fileSorted()
_avg_fear_index_vs_RuNi_10.getAvgFear()

for i,v in enumerate(_Ni_10_start):
    between_time.append(_Ni_10_stable[i]-v)
for index in range(len(_avg_fear_index_vs_RuNi_10.peopel_result_avg_fear_index)):
    #     # 对象列表获取元素--()
    speed_change_in_fear_2.append(
    round(((float)(_avg_fear_index_vs_RuNi_10.getOneAvgFear(index)) - 50.00) * 1E3 / between_time[index], 2))
print(speed_change_in_fear_2)

_Ni_40_start = [3432,2996,2581,2580,2636,2948,3264,2026,3182,2576]
_Ni_40_stable = [8240,4910,3260,3640,4070,3650,3700,2400,3470,2790]
between_time, speed_change_in_fear_3= [],[]
# 寻找test5-Ru-Ni-1文件下的.csv文件
file_dir="/var/www/html/GitHub/repository/网络反恐Netlogo仿真模型/网络反恐仿真模型/网络反恐仿真实验室/people/test11-Ru-Ni-40"
find_str_1 = "\"average fear index\""
find_str_2 = "\"person public influence\""
find_str_3 = "\"fear-sacle of people\""
Ru = [round(a*0.1,1) for a in range(1,11)]
_avg_fear_index_vs_RuNi_40=FileRead_fmg(file_dir,Ru,[],find_str_1,find_str_2,find_str_3)
_avg_fear_index_vs_RuNi_40.file_name()
_avg_fear_index_vs_RuNi_40.fileSorted()
_avg_fear_index_vs_RuNi_40.getAvgFear()

for i,v in enumerate(_Ni_40_start):
    between_time.append(_Ni_40_stable[i]-v)
for index in range(len(_avg_fear_index_vs_RuNi_40.peopel_result_avg_fear_index)):
    #     # 对象列表获取元素--()
    speed_change_in_fear_3.append(
    round(((float)(_avg_fear_index_vs_RuNi_40.getOneAvgFear(index)) - 50.00) * 1E3 / between_time[index], 2))
print(speed_change_in_fear_3)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
plt.grid(linestyle='--')
plt.xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.plot(Ru, [22.29, 0.31, 0.49, 0.63, -0.94, -3.64, -4.27, -3.89, -4.07, -4.59], 'o-', label='Ni=1')
plt.plot(Ru, [6.61, -1.1, -9.65, -14.22, 0.66, -9.76, -28.27, -29.57, -40.05, -20.15], 'o-', label='Ni=10')
plt.plot(Ru, [0.47, -1.14, -25.5, -20.64, 1.85, -49.81, -84.93, -103.04, -136.43, -189.75], 'o-', label='Ni=40')
plt.yticks(fontsize=11)
plt.xticks(fontsize=11)
plt.ylabel("Change speed in average fear index of people",fontsize=12)
plt.xlabel("Resource utilization rate",fontsize=12)
plt.title("Change speed in average fear index of people vs. Resource utilization rate & Numbers of intervation",fontsize=14)
plt.legend(bbox_to_anchor=(1,1),ncol=3,fancybox=True,fontsize=11)
# ax2.legend(bbox_to_anchor=(0.918,0.95),ncol=3,fancybox=True)
plt.show()