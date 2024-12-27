import torch


x = torch.arange(12)

# tensor
print(f'tensor: \n{x}\n')

# shape and size
print(f'shape: \n{x.shape}')
print(f'size: \n{x.size()}')

# dimension
print(f'dimension: \n{x.ndim}')

# number of elements
print(f'number of elements: \n{x.numel()}')

# tensor type
print(f'dtype: {x.dtype}')