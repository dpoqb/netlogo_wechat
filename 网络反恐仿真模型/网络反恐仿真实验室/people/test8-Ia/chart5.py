from people.FileRead import FileRead_fmg
import matplotlib.pyplot as plt

# 寻找test7-Ge下的.csv文件
file_dir='/home/songwei/桌面/网络反恐仿真实验室/people/test7-Ge'
find_str_1 = "\"average fear index\""
find_str_2 = "\"person public influence\""
find_str_3 = "\"fear-sacle of people\""
terror_event_start_1 = []
Ge = [round(a*0.1,1) for a in range(1,11)]
_avg_fear_index_vs_Ge=FileRead_fmg(file_dir,Ge,terror_event_start_1,find_str_1,find_str_2,find_str_3)
_avg_fear_index_vs_Ge.file_name()
_avg_fear_index_vs_Ge.fileSorted()
_avg_fear_index_vs_Ge.getAvgFear()

# 寻找test8-Ge下的.csv文件
file_dir='/home/songwei/桌面/网络反恐仿真实验室/people/test8-Ia'
find_str_1 = "\"average fear index\""
find_str_2 = "\"person public influence\""
find_str_3 = "\"fear-sacle of people\""
terror_event_start_1 = []
Ia = [round(a*0.1,1) for a in range(1,11)]
_avg_fear_index_vs_Ia=FileRead_fmg(file_dir,Ge,terror_event_start_1,find_str_1,find_str_2,find_str_3)
_avg_fear_index_vs_Ia.file_name()
_avg_fear_index_vs_Ia.fileSorted()
_avg_fear_index_vs_Ia.getAvgFear()


fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax1.grid(linestyle='--')
ax1.set_xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ax1.set_ylabel("The average fear index of people and media")
ax1.set_xlabel("Guidance effort")
ax1.set_title("Average fear index vs.Guidance effort")
ax1.plot(Ge,_avg_fear_index_vs_Ge.media_result_avg_fear_index,'o-',color='red',label='average fear index of media')
ax1.plot(Ge,_avg_fear_index_vs_Ge.peopel_result_avg_fear_index,'o-',label='average fear index of people')
ax1.legend(loc='2')

ax2 = fig.add_subplot(1,2,2)
ax2.grid(linestyle='--')
ax2.set_xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ax2.set_ylabel("The average fear index of people and media")
ax2.set_xlabel("Intervention ability to media")
ax2.set_title("Average fear index vs.Intervention ability to media")
ax2.plot(Ia,_avg_fear_index_vs_Ia.media_result_avg_fear_index,'o-',color='red',label='average fear index of media')
ax2.plot(Ia,_avg_fear_index_vs_Ia.peopel_result_avg_fear_index,'o-',label='average fear index of people')
ax2.legend(loc='2')

plt.show()