from hashlib import new
import pandas as pd
import numpy as np

## Removed from the input file 
## This is the beginning polymer template

polymer = 'KOKHCCHNKKFHBKVVHNPN'
poly_lst = [x for x in polymer]
poly_lst

f = open("input_day14.txt")
dict_map = {}
for newline in f:
    a, b = str.split(str.rstrip(newline), ' -> ')
    dict_map[a] = b
f.close()

def calc_new_val(tmpdict, tmplst):
    newlst = []
    for i in range(len(tmplst)-1):
        newlst.append(tmpdict[tmplst[i] + tmplst[i+1]])
    c = []
    for j in range(len(newlst)):
        c.extend(tmplst[j])
        c.extend(newlst[j])
    c.append(tmplst[len(tmplst)-1])
    return c
second_lst = calc_new_val(dict_map, poly_lst)

new_list = calc_new_val(dict_map, poly_lst)
for i in range(1, 10):
    old_list = new_list
    new_list = calc_new_val(dict_map, old_list)

len(new_list)

my_count = pd.Series(new_list).value_counts()
print(max(my_count) - min(my_count))

