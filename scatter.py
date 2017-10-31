import matplotlib.pyplot as plt

population_ages = [1, 3, 5, 7, 9, 23, 32, 44, 55, 76, 78, 98, 76, 78, 89, 90, 100, 23, 54, 56, 66, 55, 87, 67, 75, 64,
                   34]
number = [1, 3, 5, 7, 9, 23, 32, 44, 55, 76, 78, 98, 76, 78, 89, 90, 100, 23, 54, 56, 66, 55, 87, 67, 75, 64,
          34]
plt.scatter(population_ages, number, label='skiscat', color='c', s=300, marker='o')

plt.title("This is a bar chart")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
