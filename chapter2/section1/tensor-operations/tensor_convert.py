import torch
import numpy as np


'''
- torch张量(tensor) 与 numpy(ndarray) 互转
    当 torch 张量转换为 numpy 张量时
    - torch 张量和 numpy 数组将共享它们的底层内存
    - 就地操作更改一个张量也会同时更改另一个张量
- 张量 和 标量 转换
'''

print('*' * 48)
print("numpy(ndarray) and torch(tensor) convert")
a = torch.arange(12, dtype=torch.float32).reshape((3,4))
print(f'type(a): {type(a)}')
print(f'a: \n{a}')

print('a(tensor) to b(ndarray)')
b = a.numpy()
print(f'type(b): {type(b)}')
print(f'b: \n{b}')

print('b(ndarray) to c(torch)')
c = torch.tensor(b)
print(f'type(c): {type(c)}')
print(f'c: \n{c}')

print('modify element with tensor a')
print('set a[2][3] = 0')
a[2][3] = 0

print(f'a[2][3]: {a[2][3]}')
print(f'b[2][3]: {b[2][3]}')
print(f'c[2][3]: {c[2][3]}')

print(f'set b[1][2] = 100')
b[1][2] = 100
print(f'a[1][2]: {a[1][2]}')
print(f'b[1][2]: {b[1][2]}')
print(f'c[1][2]: {c[1][2]}')