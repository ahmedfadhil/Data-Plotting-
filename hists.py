import matplotlib.pyplot as plt

population_ages = [1, 3, 5, 7, 9, 23, 32, 44, 55, 76, 78, 98, 76, 78, 89, 90, 100, 23, 54, 56, 66, 55, 87, 67, 75, 64,
                   34]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8, color='c')

plt.title("This is a bar chart")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
