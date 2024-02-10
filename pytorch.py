import torch
# In practice, you'll often see scalars and vectors denoted as lowercase letters such as y or a.
# And matrices and tensors denoted as uppercase letters such as X or W.

scalar = torch.tensor(7)
print(scalar.ndim)
print(scalar.shape)

vector = torch.tensor([7,7])
print(vector.ndim)
print(vector.shape)

MATRIX = torch.tensor([[7, 7], [8, 8]])
print(MATRIX.ndim)
print(MATRIX.shape)


TENSOR = torch.tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(TENSOR.ndim)
print(TENSOR.shape)

