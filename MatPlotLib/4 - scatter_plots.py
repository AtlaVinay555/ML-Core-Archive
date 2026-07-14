import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [1,3,5,7,9]

plt.scatter(x,y,label ='Scatter!', color='k', marker = '*', s=100)

plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Graph\nSub-Title')

plt.legend()

plt.show()



