from people.FileRead import FileRead_fmg
import matplotlib.pyplot as plt

terror_event_start_1 = [5223,3222,1925,2288,3020]
Ni = [1,10,20,30,40]
color='red'
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.grid(linestyle='--')
ax1.set_xticks([1,10,20,30,40])
ax1.set_ylabel("Reach stable time")
ax1.set_xlabel("Numbers of intervation")
ax1.set_title("Stable time vs.numbers of intervation")
ax1.plot(Ni, [3977,2478,2078,1099,789], 'o-',label='time')
ax1.legend(bbox_to_anchor=(1,1),ncol=3,fancybox=True)
plt.show()