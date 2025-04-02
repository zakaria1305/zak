import pandas as pd

data = {'Nom': ['Alice', 'Bob', 'Charlie'], 'Âge': [25, 30, 35]}
df = pd.DataFrame(data)
print(df.describe())