from pylab import *
from people.FileRead import FileRead
import csv

# 网民恐惧指数散点图
# 初始状态
file_fi_init = 'Pf/init_fear-index.csv'
file_fi_end = 'Pf/end_fear-index.csv'

# 初始状态数据实例对象
init_fear_index_plt = FileRead(file_fi_init, start_row=16)
# 结束状态数据实例对象
end_fear_index_plt = FileRead(file_fi_end, start_row=16)

init_fear_index_plt.readCsvFile()
init_fear_index_plt.toArray()
people = init_fear_index_plt.x_value
fear_index = init_fear_index_plt.y_value
end_fear_index_plt.readCsvFile()
end_fear_index_plt.toArray()
people1 = end_fear_index_plt.x_value
fear_index1 = end_fear_index_plt.y_value


#网民信息真实度
file_pf_init = 'Pa/init_person_information_authenticity.csv'
file_pf_end = 'Pa/end_person_information_authenticity.csv'
with open(file_pf_init) as f3:
    rows = csv.reader(f3)
    for i,start in enumerate(rows):
        if i == 16:
            break
    person_information_authenticity  = []
    for row in rows:
        person_information_authenticity.append(row[1])
with open(file_pf_end) as f4:
    rows = csv.reader(f4)
    for i,start in enumerate(rows):
        if i == 16:
            break
    person_information_authenticity_1  = []
    for row in rows:
        person_information_authenticity_1.append(row[1])
person_information_authenticity = np.asarray(person_information_authenticity)
person_information_authenticity_1 = np.asarray(person_information_authenticity_1)

#网民信息真实度
file_rb_init = 'Rb/init_risk_perception_bias.csv'
file_rb_end = 'Rb/end_risk_perception_bias.csv'
with open(file_rb_init) as f5:
    rows = csv.reader(f5)
    for i,start in enumerate(rows):
        if i == 16:
            break
    end_risk_perception_bias  = []
    for row in rows:
        end_risk_perception_bias.append(row[1])
with open(file_rb_end) as f6:
    rows = csv.reader(f6)
    for i,start in enumerate(rows):
        if i == 16:
            break
    end_risk_perception_bias_1  = []
    for row in rows:
        end_risk_perception_bias_1.append(row[1])
end_risk_perception_bias = np.asarray(end_risk_perception_bias)
end_risk_perception_bias_1 = np.asarray(end_risk_perception_bias_1)

fig = plt.figure()

# 网民信息真实度
ax = fig.add_subplot(2,2,1)
# 修改刻度
ax.set_yticks([0.0,0.2,0.4,0.6,0.8,1.0])
plt.scatter(people,person_information_authenticity, marker = 'o',label = 'Initial')
plt.scatter(people1,person_information_authenticity_1, marker = 'o',label = 'Result')
plt.title("person-information-authenticity of people")
plt.xlabel('people')
plt.ylabel('person-information-authenticity')
plt.legend(loc = 'upper right')
plt.axhline(0.6,linestyle='--',label = "1",color = 'black')

#网民认知偏差
ax = fig.add_subplot(2,2,2)
# 修改刻度
ax.set_yticks([0.0,0.2,0.4,0.6,0.7,0.8,1.0])
plt.scatter(people,end_risk_perception_bias, marker = 'o',label = 'Initial')
plt.scatter(people1,end_risk_perception_bias_1, marker = 'o',label = 'Result')
plt.title("end-risk-perception-bias of people")
plt.xlabel('people')
plt.ylabel('risk-perception-bias')
plt.legend(loc = 'upper right')
plt.axhline(0.7,linestyle='--',label = "1",color = 'black')

#网民恐惧指数初始与结果
ax = fig.add_subplot(2,1,2)
ax.set_yticks([0,20,40,50,60,80,100])
plt.scatter(people,fear_index, marker = 'o',label = 'Initial')
plt.scatter(people1,fear_index1, marker = 'o',label = 'Result')
plt.title("terrorist-network fear-index of people")
plt.xlabel('people')
plt.ylabel('fear-index')
plt.legend(loc = 'upper right')
# 作辅助线
plt.axhline(50,linestyle='--',label = "1",color = 'black')

plt.show()

