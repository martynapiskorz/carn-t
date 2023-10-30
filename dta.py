import pandas as pd
import numpy as np

def dta (file_dta):
    data = pd.io.stata.read_stata(file_dta)
    dta = data.to_csv(file_dta)
    return dta