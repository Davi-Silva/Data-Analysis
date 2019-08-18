import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

population_ages = np.random.random((2, 40))
# print(population_ages)
x = population_ages[0, :]
# print("x =", x)
y = population_ages[1, :]
# print("y =", y)
x1 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y1 = [-5, -4, -3, -2, -1, 0, 7, 2, 3, 4, 5]

plt.scatter(
    x,
    y,
    label='Ages',
    color='#a41515'
)

plt.plot(x1, y1, color="#a41515", linewidth=3, label="JavaScript")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()