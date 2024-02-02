import torch

scalar = torch.tensor(7)
print(scalar.ndim)
print(scalar.shape)

vector = torch.tensor([7,7])
print(vector.ndim)
print(vector.shape)

matrix = torch.tensor([[7,7],[8,8]])
print(matrix.ndim)
print(matrix.shape)


tensor = torch.tensor([[[1,2,3],[4,5,6],[7,8,9]]])
print(tensor.ndim)
print(tensor.shape)