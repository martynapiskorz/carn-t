import pandas as pd

def dta (file_dta):
    data = pd.io.stata.read_stata(file_dta)
    dta = data.to_csv(file_dta)
    return dta

wave1 = dta('ca08a_1.0p_EN.dta')
print(wave1)
