import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = list(zip(names, births))

df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])

df.to_csv('./data/birth1880.csv', index=False, header=False)