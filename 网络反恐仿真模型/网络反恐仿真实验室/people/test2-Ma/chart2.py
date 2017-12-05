from people.FileRead import FileRead_fmg
import matplotlib.pyplot as plt


# 寻找test2-Ma文件下的.csv文件
file_dir="/var/www/html/GitHub/repository/网络反恐Netlogo仿真模型/网络反恐仿真模型/网络反恐仿真实验室/people/test2-Ma"
find_str_1 = "\"average fear index\""
find_str_2 = "\"person public influence\""
find_str_3 = "\"fear-sacle of people\""
terror_event_start_1 = [2621,3338,2922,3538,2342,4469,2072,2234,3219,2746]
Ma = [round(a*0.1,1) for a in range(1,11)]
_avg_fear_index_vs_Ma=FileRead_fmg(file_dir,Ma,terror_event_start_1,find_str_1,find_str_2,find_str_3)
_avg_fear_index_vs_Ma.file_name()
_avg_fear_index_vs_Ma.fileSorted()
_avg_fear_index_vs_Ma.getAvgFear()
_avg_fear_index_vs_Ma.getTime()

#寻找test3-Mp文件下的.csv文件
file_dir2="/var/www/html/GitHub/repository/网络反恐Netlogo仿真模型/网络反恐仿真模型/网络反恐仿真实验室/people/test3-Mp"
terror_event_start_2 = [3144,1584,3885,2215,3149,3011,3671,2403,2842,2657]
Mp = [round(a*0.1,1) for a in range(1,11)]
_avg_fear_index_vs_Mp=FileRead_fmg(file_dir2,Mp,terror_event_start_2,find_str_1,find_str_2,find_str_3)
_avg_fear_index_vs_Mp.file_name()
_avg_fear_index_vs_Mp.fileSorted()
_avg_fear_index_vs_Mp.getAvgFear()
_avg_fear_index_vs_Mp.getTime()

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax1.grid(linestyle='--')
ax1.set_xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
ax1.plot(Ma, _avg_fear_index_vs_Ma.peopel_result_avg_fear_index, 'o-', label='fear index')
ax1.set_ylabel("The average fear index of people",fontsize=12)
x1="Media information authenticity"+"\n"+"(a)"
ax1.set_xlabel(x1,fontsize=12)
t1="Average fear index & Stable time"+"\n"+"vs.Media information authenticity"
ax1.set_title(t1,fontsize=14)
ax2 = ax1.twinx()
ax2.plot(_avg_fear_index_vs_Ma.var, [359, 473, 723, 691, 642, 561, 494, 400, 354, 286], 'o-',color='red',label='time')
ax2.set_ylabel("Stable time",fontsize=12)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
ax1.legend(bbox_to_anchor=(1,1),ncol=3,fancybox=True,fontsize=11)
ax2.legend(bbox_to_anchor=(0.907,0.95),ncol=3,fancybox=True,fontsize=11)

ax3 = fig.add_subplot(1, 2, 2)
ax3.grid(linestyle='--')
ax3.set_xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
ax3.plot(Mp, _avg_fear_index_vs_Mp.peopel_result_avg_fear_index, 'o-', label='fear index')
ax3.set_ylabel("The average fear index of people",fontsize=12)
x2="Media public influence"+"\n"+"(b)"
ax3.set_xlabel(x2,fontsize=12)
t2="Average fear index & Stable time"+"\n"+"vs.Media public influence"
ax3.set_title(t2,fontsize=14)
ax4 = ax3.twinx()
ax4.plot(_avg_fear_index_vs_Mp.var, [463, 507, 587, 809, 617, 459, 388, 317, 311, 203], 'o-', color='red',label='time')
ax4.set_ylabel("Stable time",fontsize=12)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
ax3.legend(bbox_to_anchor=(1,1),ncol=3,fancybox=True,fontsize=11)
ax4.legend(bbox_to_anchor=(0.907,0.95),ncol=3,fancybox=True,fontsize=11)

print(_avg_fear_index_vs_Ma.between_time)
print(_avg_fear_index_vs_Mp.between_time)
plt.show()