import torch

'''
部分操作会触发不必要的内存操作，因此我们需要注意这些场景，并避免。
两个原因：
- 机器学习参数有可能会很大（数百兆），且更新频繁，因此通常希望原地更新参数
- 如果有其他引用指向了旧的内存地址，那么代码会出现一些预期外的错误
'''

a = torch.arange(12, dtype=torch.float32).reshape((3,4))
print('a: ')
print(a)

b = torch.arange(12,24, dtype=torch.float32).reshape((3,4))
print('b: ')
print(b)

print('*' * 48)
print('non-inplace operations')
id_old = id(a)
a = a + b
print('id_old == id(a): ')
print(id_old == id(a))

print('*' * 48)
print('inplace operations with [:]')
c = torch.zeros_like(a)
print('c: ')
print(c)
print(f'id(c): {id(c)}')

c[:] = a + b
print('c[:] = a + b')
print(f'id(c): {id(c)}')
# print('c: ')

print('*' * 48)
print('inplace operations with +=/-=/*=...')
d = torch.zeros_like(a)
print('d: ')
print(d)
print(f'id(d): {id(d)}')

d += a
print(f'id(d): {id(d)}')
# print('d: ')

d *= a
print(f'id(d): {id(d)}')
# print('d: ')