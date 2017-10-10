import csv
import numpy as np
import os

# 提取文件超类
class FileRead():
	def __init__(self, filepath, start_row):
		self.filepath = filepath
		self.start_row = start_row
		self.x_value = []
		self.y_value = []
	def readCsvFile(self):
		with open(self.filepath) as f:
			rows = csv.reader(f)
			for i,start in enumerate(rows):
				if i==self.start_row:
					break
			for row in rows:
				self.x_value.append(row[0])
				self.y_value.append(row[1])
	def toArray(self):
		self.x_value = np.asarray(self.x_value)
		self.y_value = np.asarray(self.y_value)

# 提取两个字符串之间的数据
class FileRead_com():
	def __init__(self,filepath,findstr_1,findstr_2):
		self.filepath = filepath
		self.row_list = {}
		self.x_value = []
		self.y_value = []   #people average fear index
		self.y_value2 = []  #medai average fear index
		self.findstr_1 = findstr_1
		self.findstr_2 = findstr_2
	def readCsvFile(self):
		with open(self.filepath) as f:
			rows = csv.reader(f)
			for i, start in enumerate(rows):
				# python逻辑运算符与C、java不一样
				try:
					if len(start):
						self.row_list[i + 1] = start
				except:
					pass
		global start_row, end_row
		for k, value in self.row_list.items():
			# print(str(k) + ':'+ str(value))
			if value[0] == self.findstr_1:
				start_row = k + 8
				# print(start_row)
			elif value[0] == self.findstr_2:
				end_row = k - 2
				break
		with open(self.filepath) as f:
			rows = csv.reader(f)
			for i, start in enumerate(rows):
				if i == start_row:
					break
			n = start_row
			for row in rows:
				n = n + 1
				if n <= end_row:
					if len(row):
						self.y_value.append(row[-3])
						self.y_value2.append(row[1])
						self.x_value.append(row[-4])
				else:
					break
	def toArray(self):
		self.x_value = np.asarray(self.x_value)
		self.y_value = np.asarray(self.y_value)
		self.y_value2 = np.asarray(self.y_value2)

# 提取fear sacle数据的对象
class FileRead_neo(FileRead_com):
	def __init__(self,filepath,findstr_1,findstr_2):
		super().__init__(filepath,findstr_1,findstr_2)
		self.fear_sacle = {}
		self.y_value=[[],[],[],[]]
	def readCsvFile(self):
		with open(self.filepath) as f:
			rows = csv.reader(f)
			for i, start in enumerate(rows):
				# python逻辑运算符与C、java不一样
				try:
					if len(start):
						self.row_list[i + 1] = start
				except:
					pass
		global start_row, end_row
		for k, value in self.row_list.items():
			# print(str(k) + ':'+ str(value))
			if value[0] == self.findstr_1:
				start_row = k + 10
				# print(start_row)
			elif value[0] == self.findstr_2:
				end_row = k - 2
				break
		with open(self.filepath) as f:
			rows = csv.reader(f)
			for i, start in enumerate(rows):
				if i == start_row:
					break
			n = start_row
			for row in rows:
				n = n + 1
				if n <= end_row:
					if len(row):
						self.y_value[0].append(row[1])
						self.y_value[1].append(row[5])
						self.y_value[2].append(row[-7])
						self.y_value[3].append(row[-3])
				else:
					break

			self.fear_sacle['Slite fear'] = self.y_value[0]
			self.fear_sacle['Moderate fear'] = self.y_value[1]
			self.fear_sacle['Extreme fear'] = self.y_value[3]
			self.fear_sacle['Server fear'] = self.y_value[2]

# 分析average fear index、stable timr与其他因素的影响关系，此类用于从多组类似的文件夹中提取相关的数据
class FileRead_fmg():
	def __init__(self,file_dir,var,terror_event_start,find_str_1='',find_str_2='',find_str_3='',**findString):
		self.file_dir=file_dir
		self.filePath=[]
		self._avg_fear_index,self.peopel_result_avg_fear_index = [], []
		self.media_result_avg_fear_index = []
		self.STime, self.to_stable_time, self.between_time = [], [], []
		self.var=var
		self.terror_event_start=terror_event_start
		self.find_str_1=find_str_1
		self.find_str_2=find_str_2
		self.find_str_3=find_str_3
		self.var_del = []
	def file_name(self):
		for root, dirs, files in os.walk(self.file_dir):
			for file in files:
				#  os.path.splitext将文件拆分为文件名+扩展名名
				if os.path.splitext(file)[1] == '.csv':
					self.filePath.append(os.path.join(root, file))
				else:
					pass

	def fileSorted(self):
		self.filePath = np.asarray(sorted(self.filePath))

	def getAvgFear(self):
		num = 0
		for p in self.filePath:
			# print(p)
			if num >= len(self.filePath):
				break
			# average fear index object
			self._avg_fear_index.append(FileRead_com(p, self.find_str_1, self.find_str_2))
			self._avg_fear_index[num].readCsvFile()
			# fear scale object
			self.STime.append(FileRead_neo(p, self.find_str_3, self.find_str_1))
			self.STime[num].readCsvFile()
			self.STime[num].toArray()
			num = num + 1
		for i in self._avg_fear_index:
			# 选取稳定值
			self.peopel_result_avg_fear_index.append(i.y_value[-1])
			self.media_result_avg_fear_index.append(i.y_value2[-1])

	def getTime(self):
		eq = {}
		for j in self.STime:
			UNSURE_TIME = []
			# 测试读取的文件路径
			# print(j.filepath)
			for r, v_list in j.fear_sacle.items():
				stable_value = int(v_list[-1])
				eq_vl = []
				for k, v in enumerate(v_list):
					if (int(v) == stable_value):
						eq_vl.append(k)
				eq[r] = eq_vl
			# 如果你想要测试，去掉下面注释，只分析一个文件
			# break
			for k, v in eq.items():
				pos = 0
				trap = []
				for i in range(pos, len(v)):
					for j in range(pos + 1, len(v)):
						if v[j] - v[i] != j - i:
							pos = i + 1
							continue
						elif (j - i) >= 100:
							trap.append(v[pos])
							break
					if len(trap) == 1:
						# 输出不同恐惧等级下fear-index达到平衡状态时的时间点,注释内容用于测试
						# print(k,pos,v[pos])
						UNSURE_TIME.append(v[pos])
						break
			self.to_stable_time.append(max(UNSURE_TIME))

		for i in range(len(self.terror_event_start)):
			self.between_time.append(self.to_stable_time[i] - self.terror_event_start[i])
		# 剔除误差较大的点
		for i, v in enumerate(self.var):
			if self.between_time[i] > 0 and self.between_time[i] < 1000:
				self.var_del.append(v)
	def getOneAvgFear(self,index):
		return self.peopel_result_avg_fear_index[index]


