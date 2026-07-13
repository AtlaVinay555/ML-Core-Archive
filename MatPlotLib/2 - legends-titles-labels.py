import matplotlib.pyplot as plt

x = [1,2,3]
y = [4,5,6]

x1 = [1,2,3]
y1 = [5,7,4]

plt.plot(x,y, label = '1st Line') # Labels for Legend
plt.plot(x1,y1, label = '2nd Line')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.title('Graph\nSub-Title')

plt.legend()

plt.show()



