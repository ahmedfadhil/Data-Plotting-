import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 5, 7, 10]
x2 = [1, 2, 3, 7, 11]
y2 = [1, 5, 8, 9, 12]

plt.bar(x1, y1, label='Bars1', color='r')
plt.bar(x2, y2, label='Bars1', color='c')

plt.title("This is a bar chart")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
