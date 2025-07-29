import numpy as np
import matplotlib.pyplot as plt
maths=np.array([88,92,80,89,100,80,60,100,80,34])
science=np.array([35,79,79,48,100,88,32,45,20,30])
plt.scatter(maths, science, color='blue', marker='o')
plt.title("SCATTERPLOT")
plt.xlabel("Maths Marks")
plt.ylabel("Science Marks")
plt.show()
