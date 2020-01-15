# 背包问题贪心算法
# 初始化函数
# 根据输入选择是否使用默认的一组数据进行演示，把重量、价值和总重量分别存入weight、price和C，并打印出来以供核对。
def Initial():
	'''确定物品重量、价值和背包总重量'''
	option = input('是否选择使用默认数据（Y/N）: ')
	if option == 'Y':
		weight = [35, 30, 60, 50, 40, 10, 25]
		price = [10, 40, 30, 50, 35, 40, 30]
		C = 150
	else:
		weight = list(map(int, input('请输入物品重量，用空格分开：').split( )))
		price = list(map(int, input('请输入相应的物品价值，用空格分开： ').split( )))
		C = int(input('请输入背包总重量限制： '))
	item = list(zip(weight,price))
	print('重量，价值：' + item.__str__() + '\n总重量限制：' + C.__str__())
	return item, C
# 三种策略
# 分别用三个函数实现了三种选择策略，函数最终返回的结果是按照相应选择方法对物品排序后的索引值，以供算法函数使用
def Weight(item):
	'''选重量最小的物品'''
	data = np.array(item)
	idex = np.lexsort([-1*data[:,1], data[:,0]])
	return idex

def Price(item):
	'''选价值最大的物品'''
	data = np.array(item)
	idex = np.lexsort([data[:,0], -1*data[:,1]])
	return idex

def Density(item):
	'''选价值密度最大的物品'''
	number = len(item)
	data = np.array(item)
	data_list = [0] * number
	for i in range(number):
		data_list[i] = (data[i,1])/(data[i,0])
	data_set = np.array(data_list)
	idex = np.argsort(-1*data_set)
	return idex
# 贪心算法
# 贪心算法函数实现了具体的问题解决过程，用初始化的数据和索引值作为参数，计算后返回一组最优化选择的结果。
def GreedyAlgo(item, C, idex):
	'''贪心算法'''
	number = len(item)
	status = [0] * number
	total_weight = 0
	total_value = 0
	for i in range(number):
		if item[idex[i],0] <= C:
			total_weight += item[idex[i],0]
			total_value += item[idex[i],1]
			status[idex[i]] = 1
			C -= item[idex[i],0]
		else:
			continue
	return total_weight, total_value, status
# 比较函数
# 比较用三种策略计算后得到结果中总价值的大小，并返回价值最高的一组结果。
def Compare(total_value1, total_value2, total_value3):
	'''比较三种结果'''
	values = zip(total_value1, total_value2, total_value3)
	data = np.array([total_value1[1], total_value2[1], total_value3[1]])
	idex = np.argsort(data)
	value = list(zip(*values))
	results = list(value[idex[2]])
	return results
# 主函数
# 主函数通过调用以上几个函数，最终实现问题的解决方案，并打印出最优结果，同时打印出三种策略各自的最优结果，以供检查。
def main():
	'''主体结构'''
	item0, C = Initial()
	item = np.array(item0)
	idex_weight = Weight(item)
	idex_price = Price(item)
	idex_Density = Density(item)
	results_weight = GreedyAlgo(item, C, idex_weight)
	print(results_weight)
	results_Price = GreedyAlgo(item, C, idex_price)
	print(results_Price)
	results_Density = GreedyAlgo(item, C, idex_Density)
	print(results_Density)
	results = Compare(results_weight, results_Price, results_Density)
	print(results)


import numpy as np

main()