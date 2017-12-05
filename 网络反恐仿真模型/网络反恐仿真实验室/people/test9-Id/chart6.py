from people.FileRead import FileRead_fmg
import matplotlib.pyplot as plt

# 寻找test9-Id下的.csv文件
file_dir="/var/www/html/GitHub/repository/网络反恐Netlogo仿真模型/网络反恐仿真模型/网络反恐仿真实验室/people/test9-Id"
find_str_1 = "\"average fear index\""
find_str_2 = "\"person public influence\""
find_str_3 = "\"fear-sacle of people\""
terror_event_start_1 = [2098,1944,1708,1496,2157]
Id = [20,60,100,140,200]
_avg_fear_index_vs_Id=FileRead_fmg(file_dir,Id,terror_event_start_1,find_str_1,find_str_2,find_str_3)
_avg_fear_index_vs_Id.file_name()
_avg_fear_index_vs_Id.fileSorted()
_avg_fear_index_vs_Id.getAvgFear()
_avg_fear_index_vs_Id.getTime()

print(_avg_fear_index_vs_Id.var)
print(_avg_fear_index_vs_Id.terror_event_start)
print(_avg_fear_index_vs_Id.to_stable_time)
print(_avg_fear_index_vs_Id.between_time)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.grid(linestyle='--')
ax1.set_xticks(Id)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
ax1.set_ylabel("Stable time",fontsize=12)
ax1.set_xlabel("Intervation delay",fontsize=12)
ax1.set_title("Stable time vs.Intervation delay",fontsize=14)
ax1.plot(_avg_fear_index_vs_Id.var,[2630, 2885, 3596, 4304, 4920],'o-',label='time')
ax1.plot([20,200],[2630,4920],'--')
ax1.legend(loc='2',fontsize=11)
plt.show()