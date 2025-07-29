import pandas as pd
data={ 'name':['Alice', 'Bob', 'Charlie'], 'age':[25,30,35], 'score':[88,76,99] }
df=pd.DataFrame(data)
print(df.loc[0:1])
