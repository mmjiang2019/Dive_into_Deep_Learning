import torch

x = torch.arange(12) # dimension: 1
# tensor
print(f'tensor xr: \n{x}\n')
# shape and size changed
print(f'shape: \n{x.shape}')
print(f'size: \n{x.size()}')
# dimension changed
print(f'dimension: \n{x.ndim}')
# number of elements not changed
print(f'number of elements: \n{x.numel()}')
# tensor type not changed
print(f'dtype: {x.dtype}')

# without copy
# change tensor shape with function reshape()
xr = x.reshape(3, 4)
# tensor
print(f'tensor xr: \n{xr}\n')
# shape and size changed
print(f'shape: \n{xr.shape}')
print(f'size: \n{xr.size()}')
# dimension changed
print(f'dimension: \n{xr.ndim}')
# number of elements not changed
print(f'number of elements: \n{xr.numel()}')
# tensor type not changed
print(f'dtype: {xr.dtype}')

# auto computation for dimention shape:
# change tensor shape with -1
xv = xr.view(-1, 6)
# tensor
print(f'tensor xv: \n{xv}\n')
# shape and size changed
print(f'shape: \n{xv.shape}')
print(f'size: \n{xv.size()}')
# dimension not changed
print(f'dimension: \n{xv.ndim}')
# number of elements not changed
print(f'number of elements: \n{xv.numel()}')
# tensor type not changed
print(f'dtype: {xv.dtype}')

# NOTE:
# is there any difference between reshape() and iew() ?