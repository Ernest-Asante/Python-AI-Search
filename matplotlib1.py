import numpy as np
import matplotlib.pyplot as plt

X_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100
 
#plt.scatter(X_data, y_data, c="blue", marker="*")
#plt.show()

years = [2006 + x for x in range(16)]
weights = [80,83,84,85,86,82,81,79,83,80,
           82,82,83,81,80,79]

#print(len(years))
#print(len(weights))

#plt.plot(years, weights)
#plt.show()

x = ["C++", "C#", "Python", "Java", "Go"]
y = [20, 50, 140, 1, 45]

plt.pie(y, labels=x)
plt.title("Programming chart")
plt.show()