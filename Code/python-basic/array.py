# 创建一个数组
score = [100, 200, 300]
print(score)
# 创建一个空数组
score1 = []
# 数组的长度
length = len(score)
print('数组的长度是:',length)
# 获取数组中的元素
print('数组中的第一个元素是:',score[0])
print('数组中的第二个元素是:',score[1])
# 获取数组中的最后一个元素
print('数组中的最后一个元素是:',score[-1])
print('数组中的倒数第二个元素是:',score[-2])
# 向数组中添加元素 [100, 200, 300]
score.append(20)
print(score) #[100, 200, 300, 20]
# 像数组中指定位置插入元素 [100, 200, 300, 20]
score.insert(1, 500)
print(score)  #[100, 500, 200, 300, 20]
# 删除数组末尾的元素
score.pop() 
print(score)
# 删除指定位置的元素  [100, 500, 200, 300]
score.pop(1) 
print(score) # [100, 200, 300]
# 替换元素 [100, 200, 300]
score[1] = 400
print(score) # [100, 400, 300]
# 向数组中添加不同的数据类型
score.append('bob')
print(score)