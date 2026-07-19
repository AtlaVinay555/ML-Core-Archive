# 1) Design model (input, output size, forward pass)

# 2) Construct loss and optimizer

# 3) Training loop
#    - forward pass: compute prediction
#    - backward pass: gradients
#    - update weights

import torch
import torch.nn as nn # Neural Network Module

#automatic gradient calculation using autograd

# f = w * x

# f = 2 * x

X = torch.tensor([[1],[2],[3],[4]],dtype=torch.float32)
Y = torch.tensor([[2],[4],[6],[8]],dtype=torch.float32)

X_test = torch.tensor([5],dtype=torch.float32)
n_samples, n_features = X.shape
print(n_samples,n_features)

input_size = n_features
output_size = n_features

# model = nn.Linear(input_size,output_size)

class LinearRegression(nn.Module): # custom function

    def __init__(self, input_dim, output_dim):
        super(LinearRegression, self).__init__()

        # define layers
        self.lin = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.lin(x)


model = LinearRegression(input_size, output_size)

#gradient
# MSE = 1/n * (w*x - y)**2

print(f'Prediction before training: f(5) = {model(X_test).item():.3f}')

#Training 

learning_rate = 0.01
n_iters = 1000 # Prediction = 9.999 for 10 and 10.000 for 20

loss = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(),lr = learning_rate)

#more iterations needed for correct calculation (> manual)

for epoch in range(n_iters):
  # prediction = forward pass
  y_pred = model(X)

  #loss
  l = loss(Y,y_pred)

  #gradients 
  l.backward() #gradient of loss w.r.t w

  #update weights
  optimizer.step()

  #zero gradients again
  optimizer.zero_grad()

  if epoch % 10 == 0:
    [w,b] = model.parameters()
    print(f'epoch {epoch+1}: w = {w[0][0].item():.3f} , loss = {l:.8f}')

print(f'Prediction after training: f(5) = {model(X_test).item():.3f}')