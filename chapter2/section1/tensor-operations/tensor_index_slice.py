import torch

'''
和任何 Python 数组中一样，张量中的元素可以通过索引访问
- 第一个元素的索引是0，最后一个元素索引是-1
- 可以指定范围以包含第一个元素和最后一个之前的元素 —— 切片
'''
print('*' * 48)
print('tensor indexing')
x = torch.randint(0, 10, [4, 2, 3])
print("x: ")
print(x)

'''
如果第 n 维度的长度为 dn，则索引的可取值范围为：
[-dn-1, dn-1]
'''
print("x[0]: ")
print(x[0])

print("x[-1]: ")
print(x[-1])

print("x[0, 1]: ")
print(x[0, 1])

print("x[3, 1, 2]: ")
print(x[3, 1, 2])

print("x[-4, -2, -3]: ")
print(x[-4, -2, -3])

'''
切片操作
- 显示指定一个或多个维度的范围
- 隐式指定一个或多个维度的范围
- 显式、隐式相互组合
'''
print("*" * 48)
print('tensor indexing')

x = torch.arange(24).reshape(2,3,4)
print("x: ")
print(x)

print("explicitly specifying the range of dimensions")
print("without step set: ")
print("x[0:1, 1:2]: ")
print(x[0:1, 1:2])

print("with step set: ")
print("x[0:1:1, 1:2:2]: ")
print(x[0:1:1, 1:2:2])

print("without step set: ")
print("x[0:1, 1:2, 2:4]: ")
print(x[0:1, 1:2, 2:4])

print("with step set: ")
print("x[0:1:1, 1:2:2, 2:4:3]: ")
print(x[0:1:1, 1:2:2, 2:4:3])


print("*" * 48)
print("implicitly specifying the range of dimensions")
print("implict start: ")
print("x[:-1] ")
print(x[:-1])

print("implict end: ")
print("x[1:] ")
print(x[1:])

print("implict start and end: ")
print("x[:] ")
print(x[:])
