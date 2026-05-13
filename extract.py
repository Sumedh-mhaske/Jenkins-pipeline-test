import pandas as pd

print('Extract data')

data = {
    'Id': [1, 2, 3],
    'Name': ['Raja', 'Rani', 'Chaplin'],
    'Age': [20, 30, 40]
}

df = pd.DataFrame(data)

print(df)
