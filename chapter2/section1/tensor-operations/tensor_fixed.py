import torch


# tensor filled with uncertain values
print(f'empty tensor: ')
print(torch.empty((2, 3, 4)))

# tensor filled with 0
print(f'zeros tensor: ')
print(torch.zeros((2, 3, 4)))

# tensor filled with 1
print(f'ones tensor: ')
print(torch.ones((2, 3, 4)))

# tensor filled with target
print(f'tensor filled with target: ')
print(torch.full((2, 3, 4), 9))


x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(f'tensor x: ')
print(x)

# tensor filled with uncertain values with same shape as x
print(f'tensor empty_like x: ')
print(torch.empty_like(x))

# tensor filled with 0 with same shape as x
print(f'tensor zeros_like x: ')
print(torch.zeros_like(x))

# tensor filled with 1 with same shape as x
print(f'tensor ones_like x: ')
print(torch.ones_like(x))

# tensor filled with target value with same shape as x
print(f'tensor full_like x: ')
print(torch.full_like(x, 16))

print(f'random integers with uniform distribution in [low, high): ')
print(f'low = 3, high = 6: ')
print(torch.randint(3, 6, [3, 4]))

# tensor filled with random numbers from a uniform distribution on the interval [0, 1)
print(f'uniform distribution tensor on [0, 1): ')
print(torch.rand((2, 3, 4)))

# tensor filled with random numbers from a normal distribution with mean 0 and variance 1 (also called the standard normal distribution)
print(f'standard normal distribution tensor: ')
print(torch.randn((2, 3, 4)))

# tensor filled with given lists
print(f'tensor from given lists: ')
print(torch.tensor([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]))
