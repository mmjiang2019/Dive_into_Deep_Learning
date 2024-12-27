import torch


x = torch.tensor([-1.0, -2, 4, 8])
print(f'x: {x}')

y = torch.tensor([2, -2, -2, 2])
print(f'y: {y}')

print('unary arithmetic operations')
print(f'absolute value')
print(f'x.abs(): ')
print(x.abs())

print(f'square root')
print(f'x.sqrt(): ')
print(x.sqrt())

print(f'square function')
print(f'x.square(): ')
print(x.square())

print(f'exponential funcion')
print(f'x.exp(): ')
print(x.exp())

print(f'exponential minus one')
print(f'x.expm1(): ')
print(x.expm1())

print(f'natual logarithm')
print(f'x.log(): ')
print(x.log())

print(f'logarithm of 1 plus x')
print(f'x.log1p(): ')
print(x.log1p())

print(f'sign function')
print(f'x.sign(): ')
print(x.sign())

print(f'round function')
print(f'x.round(): ')
print(x.round())

print(f'floor function')
print(f'x.floor(): ')
print(x.floor())


# binary arithmetic operations
print('binary arithmetic operations')
print(f'x + y[x.add(y)]: ')
print(x.add(y))
# print(x + y)

print(f'x - y[x.subtract(y)]: ')
print(x.subtract(y))
# print(x - y)

print(f'x * y[(x.multiply(y)]: ')
print(x.multiply(y))
# print(x * y)

print(f'x / y[x.divide(y)]: ')
print(x.divide(y))
# print(x / y)

print(f'x // y: ')
print(x // y)

print(f'x % y[x.remainder(y)]: ')
print(x.remainder(y))
# print(x % y)

print(f'x ** y[x.pow(y): ')
print(x.pow(y))

print('*'*36)
print(f'comparison with bool tensor result returned: ')
print(f'x == y[x.eq(y)]: ')
print(x.eq(y))
# print(x == y)

print(f'x > y[x.greater(y): ')
print(x.greater(y))
# print(x > y)

print(f'x >= y[x.greater_equal(y): ')
print(x.greater_equal(y))
# print(x >= y)

print(f'x < y[x.less(y): ')
print(x.less(y))
# print(x < y)

print(f'x <= y[x.less_equal(y): ')
print(x.less_equal(y))
# print(x <= y)


print('*'*36)
print(f'bitwise operations(integers only): ')
a = torch.arange(1, 5).reshape(2, 2)
print(f'a: ')
print(a)

b = torch.arange(-1, 3).reshape(2, 2)
print(f'b: ')
print(b)

print(f'a & b[a.bitwise_and(b)]: ')
print(a.bitwise_and(b))
# print(a & b)

print(f'a | b[a.bitwise_or(b)]: ')
print(a.bitwise_or(b))
print(a | b)

print(f'a ^ b[a.bitwise_xor(b)]: ')
print(a.bitwise_xor(b))
print(a ^ b)

print(f'a << b[a.bitwise_left_shift]: ')
print(a.bitwise_left_shift(b))
# print(a << b)

print(f'a >> b[a.bitwise_right_shift]: ')
print(a.bitwise_right_shift(b))
# print(a >> b)