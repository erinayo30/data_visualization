import matplotlib.pyplot as plt
import seaborn as sns


sns.set()

# plt.style.available
# ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery']

x_values =[1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(2, 4, s=200)
ax.scatter(x_values, y_values, s=100)
# ax.plot(input_values, squares, linewidth=3)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.scatter(2, 4)
# set size of tick labels
ax.tick_params(labelsize=14)

plt.show()