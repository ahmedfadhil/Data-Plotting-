import matplotlib.pyplot as plt
import csv
import numpy as np

# x = []
# y = []
#
# # with open('data', 'r') as csvfile:
# #     plots = csv.reader(csvfile, delimiter=',')
# #     for row in plots:
# #         x.append(int(row[0]))
# #         y.append(int(row[1]))
# # plt.plot(x, y, label='Loaded from file')

# Clean code with numpy
x, y = np.loadtxt('data', delimiter=',', unpack=True)
plt.plot(x, y, label='Loaded from file')

plt.title("This is a bar chart")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
