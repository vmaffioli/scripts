import pandas as pd
import re

path = input('Insira o caminho do arquivo:')

if len(path) > 0:
    if re.search('\\b.xlsx\\b', path, re.IGNORECASE):
        df_excel = pd.read_excel(path)
        df_excel.to_json(path.replace(".xlsx", ".json"))
        
    elif re.search('\\b.csv\\b', path, re.IGNORECASE):
        df_csv = pd.read_csv(path)
        df_csv.to_json(path.replace(".csv", ".json"))
        
    else:
        print('Arquivo invalido')

else:
    print('Arquivo invalido')