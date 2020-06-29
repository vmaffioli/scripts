import pandas as pd
df_excel = pd.read_excel('teste.xlsx')
df_excel.to_json('teste.json')


