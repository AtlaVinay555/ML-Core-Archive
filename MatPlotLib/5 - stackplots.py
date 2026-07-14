import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleepin = [7,4,7,2,5]
eatin = [2,3,5,2,2]
workin = [7,8,9,3,2]
playin = [8,6,3,2,1]

# no lables but empty plots present

plt.plot([],[],color='m',label='Sleeping', linewidth = 5)
plt.plot([],[],color='c',label='Eating', linewidth = 5)
plt.plot([],[],color='r',label='Working', linewidth = 5)
plt.plot([],[],color='k',label='Playing', linewidth = 5)

plt.stackplot(days,sleepin,eatin,workin,playin,colors=['m','c','r','k'])



plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Graph\nSub-Title')

plt.legend()

plt.show()



