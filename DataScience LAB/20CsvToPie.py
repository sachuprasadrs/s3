import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('olympics.csv')
country_data = df['country']
medal_data = df['gold medal']
plt.pie(medal_data, labels=country_data)
plt.title('SUMMER OLYMPICS 2016 - GOLD MEDALS')
plt.show()
