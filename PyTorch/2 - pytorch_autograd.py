import torch

x = torch.randn(3, requires_grad=True)

print(x)

y = x + 2 # BackPropagation + Addition

print(y)

z = y * 2 # MulBackWard

z = z.mean() # MeanBackWard

v = torch.tensor([0.1,0,2,0.001])

z.backward() #dz/dx {Can pass v here if not z.mean() [mv]}

# Grad can be implicitly created only for Scalar Outputs

print(x.grad) # Gradient of x

# In bg, it does a Vector Jacobian Product to get them.

# If z is not a scalar arg, we must give it a vector (v)

# How to stop Gradient Type Tracking by torch?
# (Stop it from tracking history in Computational Graph)

# -> (1) x.requires_grad_(False)
# -> (2) x.detatch() {creates new tensor that does not need gradient}
# -> (3) with torch.no_grad():

x.requires_grad_(False) # The "_" before false -> inplace

print(x)

x1 = x.detatch()

print(y)

with torch.no_grad():
  y = x + 2

print(y)

weights = torch.ones(4, requires_grad=True)

for epoch in range(3): #optimization function
    model_output = (weights * 3).sum()

    model_output.backward() # will again write to .grad

    print(weights.grad) # gives updated wrong values 

    weights.grad.zero_() # so we reset them after (1)

# This is very important during training

optimizer = torch.optim.SGD(weights,lr=0.01)
optimizer.step()
optimizer.zero_grad() # reset like above example





