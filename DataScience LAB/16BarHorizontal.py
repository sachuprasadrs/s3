import numpy as np
import matplotlib.pyplot as plt
x=np.array(['Java','Python','PHP','Javascript','C#','C++'])
y=np.array([22.2,17.6,8.8,8,7.7,6.7])
colors=['#b07219', '#3572A5','#8892be','#f1e05a', '#178600','blue']
plt.barh(x,y,color=colors)
plt.title('Horizontal Bar Chart')
plt.xlabel('Programming Language')
plt.ylabel('Popularity')
plt.show()
