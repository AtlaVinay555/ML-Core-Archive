import numpy as np
import torch

'''
a = torch.rand(2,2)
b = torch.ones(2,2, dtype=torch.float64)
b.div_(a)
a_reshaped = a.view(-1,1)
b_np = b.numpy()
x = np.ones(15)
x_torch = torch.from_numpy(x).to(torch.int64)
print(x_torch)

if torch.cuda.is_available():
  device = torch.device('cuda')
  a_gpu = torch.ones(5,device=device)
  b_gpu = torch.ones(10)
  b_gpu = b_gpu.to(device)
  c_gpu = torch.rand(10)
  c_cpu = c_gpu.to("cpu")
  print(c_cpu.numpy())


p = torch.randn(5,requires_grad=True)

q = p + 2
r = q * 2
r = r.mean()

q.backward()

print(p.grad())

with torch.no_grad():
  q = p + 2

weights = torch.ones(4,requires_grad=True)

for epoch in range(3):
  model_output = (weights * 2).sum()
  model_output.backward()

  weights.grad.zero_()



h = torch.tensor(2.0)
i = torch.tensor(3.0)

j = torch.tensor(1.0, requires_grad=True)

i_hat = j * h

l = (i_hat - i)**2

l.backward()

print(j.grad)

'''

X = torch.tensor([1,2,3,4],dtype=torch.float32)
Y = torch.tensor([5,6,7,8],dtype=torch.float32)

W = torch.tensor(0.0,dtype=torch.float32,requires_grad=True)

def forward(X):
  return X * W

def loss(Y,Y_pred):
  return ((Y_pred - Y)**2).mean()

l_r = 0.01
iterations = 1000

for epoch in range(iterations):
  Y_pred = forward(X)
  l = loss(Y,Y_pred)

  l.backward()

  with torch.no_grad():
    W -= l_r * W.grad

  W.grad.zero_()

  print(W.grad)

print(f"Final Weight: {W.item():.3f}")





