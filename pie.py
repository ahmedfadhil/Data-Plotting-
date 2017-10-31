import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleep', 'work', 'eat', 'play']
cols = ['m', 'r', 'c', 'b']

plt.pie(slices, labels=activities, colors=cols, startangle=90, shadow=True, explode=(0, 0.1, 0, 0), autopct='%1.1f%%')


plt.title("This is a bar chart")
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()
plt.show()



# import matplotlib.pyplot as plt
#
# slices = [7,2,2,13]
# activities = ['sleeping','eating','working','playing']
# cols = ['c','m','r','b']
#
# plt.pie(slices,
#         labels=activities,
#         colors=cols,
#         startangle=90,
#         shadow= True,
#         explode=(0,0.1,0,0),
#         autopct='%1.1f%%')
#
# plt.title('Interesting Graph\nCheck it out')
# plt.show()
