import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleepin = [7,4,7,2,5]
eatin = [2,3,5,2,2]
workin = [7,8,9,3,2]
playin = [8,6,3,2,1]

slices = [7,2,2,13]
activities = ['sleepin','eatin','workin','playin']
cols = ['c','m','r','b']

plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,explode=(0,0.1,0,0),autopct='%1.1f%%')

#plt.xlabel('X Axis')

#plt.ylabel('Y Axis')

plt.title('Graph\nSub-Title')

#plt.legend()

plt.show()



