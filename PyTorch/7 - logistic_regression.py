# 1) Design model (input, output size, forward pass)

# 2) Construct loss and optimizer

# 3) Training loop
#    - forward pass: compute prediction and loss
#    - backward pass: gradients
#    - update weights

import torch
import torch.nn as nn

import numpy as np

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

# 0 -> Prepare data

bc = datasets.load_breast_cancer() #binary classification
X,Y = bc.data,bc.target

n_samples, n_features = X.shape

X_train, X_test , Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=1234)

#scale

sc = StandardScaler() # make our features to have zero mean and unit variance for equality

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

X_train = torch.from_numpy(X_train.astype(np.float32))
X_test = torch.from_numpy(X_test.astype(np.float32))
Y_train = torch.from_numpy(Y_train.astype(np.float32))
Y_test = torch.from_numpy(Y_test.astype(np.float32))

Y_train = Y_train.view(Y_train.shape[0], 1) # 1 r 1 c
Y_test = Y_test.view(Y_test.shape[0], 1)

# 1 -> Model

# f = wx + b, sigmoid func at end (will return val->[0,1])

class LogisticRegression(nn.Module):

    def __init__(self, n_input_features):
        super(LogisticRegression, self).__init__()
        self.linear = nn.Linear(n_input_features, 1)

    def forward(self, x):
        y_predicted = torch.sigmoid(self.linear(x))
        return y_predicted


model = LogisticRegression(n_features)


# 2 -> Loss and Optimizer

criterion = nn.BCELoss()
learning_rate = 0.01

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=learning_rate
)

# 3 -> Training Loop

num_epochs = 100

for epoch in range(num_epochs):

    # Forward pass and loss
    y_predicted = model(X_train)
    loss = criterion(y_predicted, Y_train)

    # Backward pass
    loss.backward()

    # Update weights
    optimizer.step()

    # Zero gradients
    optimizer.zero_grad()

    if (epoch + 1) % 10 == 0:
        print(f'epoch: {epoch + 1}, loss = {loss.item():.4f}')

# Evaluation

with torch.no_grad():
  predicted = model(X_test)
  y_predicted_cls = predicted.round()
  acc = (y_predicted_cls == Y_test).sum().item() / Y_test.shape[0]

print(f'accuracy:{acc:.4f}')


