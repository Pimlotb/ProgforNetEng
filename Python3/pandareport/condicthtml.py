import pandas as pd

a = {'Job1': {'2017-01-10': [44, 33, 11, 75, 22]}, 
'Job2': {'2017-01-05': [25, 25, 0, 100, 25], '2017-01-10': [50, 50, 0, 100, 25]}, 
'Job3': {'2017-01-03': [44, 22, 22, 50, 22], '2017-01-04': [66, 36, 30, 54, 22], '2017-01-06': [88, 52, 36, 59, 22], '2017-01-10': [132, 68, 64, 51, 22], '2017-01-02': [22, 9, 13, 40, 22], '2017-01-08': [110, 52, 58, 47, 22]},
 'Job4': {'2017-01-10': [25, 25, 0, 100, 25]}}
df = pd.DataFrame(data=a)
df = df.fillna(' ').T
print (df.to_html())
