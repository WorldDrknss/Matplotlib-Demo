import matplotlib.pyplot as plt
plt.style.use('seaborn')
fig, ax = plt.subplots()
x_value = [1, 2, 3, 4, 5]
y_value = [1, 4, 9, 16, 25]
ax.scatter(x_value, y_value, c='red', s=50)

ax.set_title("Scattered")
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=10)

plt.show()