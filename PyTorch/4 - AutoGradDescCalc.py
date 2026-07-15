import numpy as np


#automatic gradient calculation using autograd

# f = w * x

# f = 2 * x

X = np.array([1,2,3,4],dtype=np.float32)
Y = np.array([2,4,6,8],dtype=np.float32)

w = 0.0

# model prediction

def forward(x):
  return w*x #forward pass

#loss = MSE (for Linear Regression)

def loss(y,y_predicted):
  return ((y_predicted - y)**2).mean()

#gradient
# MSE = 1/n * (w*x - y)**2

def gradient(x,y,y_predicted):
  return np.dot(2*x,y_predicted - y).mean() #dJ/dw = 1/n * 2x (w*x - y)

print(f'Prediction before training: f(5) = {forward(5):.3f}')

#Training 

learning_rate = 0.01
n_iters = 20 # Prediction = 9.999 for 10 and 10.000 for 20

for epoch in range(n_iters):
  # prediction = forward pass
  y_pred = forward(X)

  #loss
  l = loss(Y,y_pred)

  #gradients 
  dw = gradient(X,Y,y_pred)

  #update weights
  w -= learning_rate * dw

  if epoch % 1 == 0:
    print(f'epoch {epoch+1}: w = {w:.3f} , loss = {l:.8f}')

print(f'Prediction after training: f(5) = {forward(5):.3f}')