import numpy as np
import matplotlib.pyplot as plt
x = np.array([3, 12, 28, 45])
y = np.array([15, 70, 85, 120])
x1 = np.array([8, 22, 35, 50])
y1 = np.array([40, 90, 100, 130])
plt.plot(x,y, color='red', marker='o', mfc='blue', mec='black')
plt.plot(x1,y1, color='blue', marker='o', mfc='red', mec='black')
plt.title('Legend Diagram')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.show()
