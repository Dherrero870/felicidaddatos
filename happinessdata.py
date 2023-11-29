import pandas as pd
xl_file = pd.ExcelFile("Chapter2OnlineData.xls")  
with pd.ExcelFile("Chapter2OnlineData.xls") as xls:  
    df1 = pd.read_excel(xls, "Table2.1") 
    print (df1.head(10))
    columnas = df1.columns.tolist()
print("Listado de columnas:")
for columna in columnas:
    print(columna)