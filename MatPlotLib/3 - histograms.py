import matplotlib.pyplot as plt

ages = [22,32,54,34,24,42,41,19,5,12,31,53,52,101]

# age_ids = [x for x in range (len(ages))]

# plt.bar(age_ids,ages, label = "Age Distribution")

bins_for_histogram = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(ages,bins_for_histogram, histtype='bar', rwidth= 0.8)

plt.title('Graph\nSub-Title')

plt.legend()

plt.show()



