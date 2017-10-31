import matplotlib.pyplot as plt

days = [1, 3, 5, 7, 9]
sleeping = [1, 3, 3, 5, 4]
working = [1, 3, 55, 7, 9]
eating = [1, 3, 6, 7, 9]
playing = [1, 3, 9, 7, 10]

plt.plot([], [], color='m', label='Sleeping', linewidth=5)
plt.plot([], [], color='r', label='Working', linewidth=5)
plt.plot([], [], color='c', label='Eating', linewidth=5)
plt.plot([], [], color='k', label='Playing', linewidth=5)

plt.stackplot(days, sleeping, working, eating, playing, colors=['m', 'r', 'c', 'k'])

plt.title("This is a bar chart")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
