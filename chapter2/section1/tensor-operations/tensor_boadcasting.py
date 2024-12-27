import torch


'''
相同维度
广播规则如下：
- 从后向前检查维度
从最后一个维度开始，比较两个张量的对应维度大小。
- 维度大小必须相同或其中一个为 1
- 如果两个维度的大小相同，则继续检查前一个维度。
- 如果其中一个维度的大小为 1，则该维度可以“广播”到另一个张量的大小。
- 如果所有维度都满足上述条件
满足以上条件，则两个张量可以进行广播并进行按元素运算。
'''
print("*" * 48)
print("broadcasting with same dimension:")
a = torch.arange(3).reshape((3, 1))
print("a: ")
print(a)

b = torch.arange(2).reshape((1, 2))
print("b: ")
print(b)

print("a + b: ")
print(a + b)


x = torch.arange(6).reshape(1, 2, 3)
print("x: ")
print(x)

y = torch.arange(6).reshape(2, 1, 3)
print("y: ")
print(y)

print(f'x * y: ')
print(x * y)


'''
不同维度张量的广播规则
- 如果两个数组的维度数不相同，则需要在维度数少的数组前面补1，直到两个数组的维度数相同。
- 从后往前比较每个维度的大小，对于两个数组形状中相同的维度，如果它们的大小相同，或者其中一个的大小为1（需要在这个维度上进行“广播”），则这两个数组在该维度上是兼容的。
- 如果两个数组在所有维度上都是兼容的，则它们可以通过广播机制进行运算；否则，会抛出异常。
'''
print("*" * 48)
print("broadcasting with different dimension:")
t1 = torch.arange(6).reshape(1, 2, 3)
print("t1: ")
print(t1)

t2 = torch.arange(6).reshape(2, 1, 3)
print("t2: ")
print(t2)

t3 = torch.arange(6).reshape(2, 3, 1)
print("t3: ")
print(t3)

t4 = torch.arange(6).reshape(2, 3)
print("t4: ")
print(t4)

print("t1 + t4: ")
print(t1 + t4)

print("t2 + t4: ")
print(t2 + t4)

print("t3 + t4: ")
try:
    print(t3 + t4)
except RuntimeError as e:
    print(e)