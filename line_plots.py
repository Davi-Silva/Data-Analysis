import matplotlib as mpl
import matplotlib.pyplot as plt

years = list(map(str, range(1980, 2019)))
print(years)

df_canada.loc['Haiti', years].plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()