import pandas as pd 
import numpy as np


df = pd.read_csv("input_day7.txt", header=None)
inputarr = np.array(df.iloc[0,:])

m1 = max(inputarr)
m0 = min(inputarr)

def compute_fuel(startval, arr1):
    arr2 = abs(np.array(arr1) - startval)
    return sum(arr2)

compute_fuel(5, [1, 2, 3])

lst = []
for i in range(m0, m1):
    lst.append(compute_fuel(i, inputarr))

min(lst)
