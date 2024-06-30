import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plotting examples
plt.figure(figsize=(10, 6))

# Example 1: Line plot
plt.subplot(3, 4, 1)
plt.plot(x, y)
plt.title('Line Plot')

# Example 2: Scatter plot
plt.subplot(3, 4, 2)
plt.scatter(x, y)
plt.title('Scatter Plot')

# Example 3: Histogram
plt.subplot(3, 4, 3)
plt.hist(y, bins=20)
plt.title('Histogram')

# Example 4: Bar plot
plt.subplot(3, 4, 4)
plt.bar(x[:10], y[:10])
plt.title('Bar Plot')

# Example 5: Pie chart
plt.subplot(3, 4, 5)
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')

# Example 6: Box plot
plt.subplot(3, 4, 6)
plt.boxplot(y)
plt.title('Box Plot')

# Example 7: Violin plot
plt.subplot(3, 4, 7)
plt.violinplot(y)
plt.title('Violin Plot')

# Example 8: Heatmap
plt.subplot(3, 4, 8)
data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.title('Heatmap')

# Example 9: 3D plot
from mpl_toolkits.mplot3d import Axes3D
ax = plt.subplot(3, 4, 9, projection='3d')
ax.plot3D(x, y, np.zeros_like(x))
ax.set_title('3D Plot')

# Example 10: Contour plot
plt.subplot(3, 4, 10)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)
plt.contour(X, Y, Z)
plt.title('Contour Plot')

plt.tight_layout()
plt.show()
