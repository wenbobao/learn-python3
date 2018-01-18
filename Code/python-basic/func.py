# 调用系统函数
a = abs(100)
print(a)
b = abs(-20)
print(b)
c = max(1,2)
print(c)
d = int('123')
print(d)
e = hex(255)
print(e)

# 定义函数
def test1():
    print("I'm function!")

def test2(num1, num2):
    return max(num1, num2)
 
test1()
print(test2(1,2))

# 定义空函数
def nop():
    pass

# 对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#  返回多个值

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x,y)

#  实际上是返回一个元组
r = move(100, 100, 60, math.pi / 6)
print(r)

# 定义默认参数

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))
print(power(5,3))

# 定义可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 递归函数

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(1))
print(fact(5))
