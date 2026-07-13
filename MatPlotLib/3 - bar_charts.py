import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [1,3,5,7,9]

x1 = [1,3,5,7,9]
y1 = [2,4,6,8,10]


plt.bar(x,y, label = 'Bars 1', color ='r')
plt.bar(x1,y1, label = 'Bars 2', color ='c')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.title('Graph\nSub-Title')

plt.legend()

plt.show()



