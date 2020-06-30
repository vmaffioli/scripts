import pandas as pd
import re
import os.path

def excel_csv_to_json(file_path):
       
    if file_exists(file_path) == True:
        if re.search('\\b.xlsx\\b', file_path, re.IGNORECASE):
            df_excel = pd.read_excel(file_path)
            df_excel.to_json(file_path.replace(".xlsx", ".json"))
            result = 0
                    
        elif re.search('\\b.xls\\b', file_path, re.IGNORECASE):
            df_excel = pd.read_excel(file_path)
            df_excel.to_json(file_path.replace(".xls", ".json"))
            result = 0
            
        elif re.search('\\b.csv\\b', file_path, re.IGNORECASE):
            df_csv = pd.read_csv(file_path)
            df_csv.to_json(file_path.replace(".csv", ".json"))
            result = 0
            
        else:
            result = 1
            
    else:
        result = 1     
            
    return result 


def file_exists(file_path):
    try:
        with open(file_path, 'r') as f:
            return True
        
    except FileNotFoundError as e:
        return False
    
    except IOError as e:
        return False

    