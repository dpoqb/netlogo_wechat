import numpy as np
import matplotlib.pyplot as plt

data = [[ 96, 7, 1, 0],
        [ 4, 32, 8, 0],
        [ 0, 61, 89, 4],
        [ 0, 0, 2, 96],
       ]
data.reverse()

columns = ('no intervention', 'slight intervention', 'moderate intervention', 'strong intervention')
rows = ['extreme fear(70~100)','server fear(50~70)','moderate fear(20~50)','slight fear(0~20)',]
# values=np.arange(0,105,5)
# value_increment=5

#得到一些柔和色调的颜色
colors = plt.cm.BuPu(np.linspace(0.2,0.6,len(rows)))
n_rows = len(data)
print(colors)
index = np.arange(len(columns)) + 0.3
bar_width = 0.4

#初始化堆积条形图垂直偏移。
y_offset = np.zeros(len(columns))

# 绘制直方图和创建表格
cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x/1.0) for x in data[row]])
#反转颜色和文本标签在顶部显示的最后一个值。
colors = colors[::-1]
cell_text.reverse()
#添加表在轴的底部
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom',
                      )
# 设置字体大小
the_table.auto_set_font_size(False)
the_table.set_fontsize(10)

#调整布局：
plt.subplots_adjust(left=0.2,bottom=0.2)
plt.ylabel("Distribution of fear range")
plt.grid(linestyle='--')
# values*value_increment值传入%d
# plt.yticks([0,20,40,60,80,100])
plt.xticks([])
plt.title("Different levels of intervention vs. Fear range")
plt.show()


