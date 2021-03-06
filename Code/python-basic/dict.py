# 创建一个字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)

# 向字典中插入值
d['Adam'] = 67
print(d)

# 删除字典中的key
d.pop('Bob')
print(d)

# 如果插入的值，字典中存在，会覆盖之前的值。
d['Bob'] = 25
print(d)

# 如果key不存在，会报错
print(d['Bob'])
# print(d['aa'])  # 报错

# 如何避免key不存在，报错的问题
# method 1

if 'Thomas' in d:
    print(d['Thomas'])
else:
    print('不存在')

# method 2
# 如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas')) 
print(d.get('Thomas', 'Thomas')) 