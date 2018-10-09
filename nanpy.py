import numpy

# martrix = numpy.array([[1,2,3],[1,2,3],[1,2,3]])
# martrix1 = numpy.array([1,2,3,4,5,6])
# mar = numpy.array(["1","2","3"])
# #　打印数组结构
# print(martrix.shape)
# # 查看类型
# # print(mar.dtype)
# # 判断数组中是否存在某个数
# # print(martrix == 2)
# # 转换类型
# mar = mar.astype(float)
# # print(mar.dtype)
# print(martrix)
# # 对行求和
# print(martrix.sum(axis=1))
# # 对列求和
# print(martrix.sum(axis=0))
# # 创建矩阵并改变形状
# a = numpy.arange(15).reshape(3,5)
# print(a)
# # 创建零矩阵
# zero = numpy.zeros((3,4))
# print(zero)
# # 创建1矩阵
# one = numpy.ones((3,3),dtype=numpy.int32)
# print(one)
# print(one.dtype)
# # 起始值，终点值，步进值
# np1 = numpy.arange(0,50,10)
# print(np1)
#
# ran = numpy.random.random((2,3))
# print(ran)
# # 从0道2pi平均取100个数
# from numpy import pi
# arr = numpy.linspace(0,2*pi,100)
# print(arr)
# #　数组四则是对应位置运算
#
# # 矩阵乘法
# A = numpy.arange(4)
# B=A
# C = numpy.dot(A,B)
# D = A.dot(B)
# print(A,B)
# print(C,D)

# 矩阵运算
# # 求e的幂
# print(numpy.exp(A))
# # 开平方
# print(numpy.sqrt(A))
# 向下取整
# b = numpy.floor(10*numpy.random.random((3,4)))
# # print(b)
# # # 把矩阵编程向量
# # print(b.ravel())
# # print(b.T)
# # # -1表示自动计算每列有多少元素
# # print(b.reshape(2,-1))

# 拼接矩阵
# a = numpy.floor(10*numpy.random.random((3,4)))
# b = numpy.floor(10*numpy.random.random((3,4)))
# print("*"*10)
# print(a)
# print("*"*10)
# print(b)
# print("*"*10)
# # 横向拼接
# print(numpy.hstack((a,b)))
# print("*"*10)
# # 纵向拼接
# print(numpy.vstack((a,b)))

# 复制
# a = numpy.arange(10)
# print("-"*10)
# print(a)
# c = a.view()
# print("-"*10)
# print(c)
# print(id(c))
# print(id(a))

# 扩展几倍

# a = numpy.array([[1,2],[3,4]])
# print(a)
# print("-"*50)
#
# b = numpy.tile(a,(2,2))
# print(b)

# 排序

a = numpy.floor(10*numpy.random.random((3,4)))
print(a)
print("-"*50)
b = numpy.sort(a,axis=1)
print(b)

print("*"*20)
c = numpy.array([2,5,6,4,7])
# 最小值索引
print(numpy.argsort(c))