import matplotlib.pyplot as plt

'''
import csv

x = []
y = []

with open('7-sample.txt','r') as csvfile:
  plots = csv.reader(csvfile,delimiter=',')
  for row in plots:
    x.append(int(row[0]))
    y.append(int(row[1]))

plt.plot(x,y,label='Loaded from sample.txt!')

'''

# With numpy

import numpy as np

x,y = np.loadtxt('7-sample.txt',delimiter=',',unpack=True)

plt.plot(x,y,label='Loaded from sample.txt!')

plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Graph\nSub-Title')

plt.legend()

plt.show()



