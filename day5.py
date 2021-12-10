import numpy as np
from numpy.lib.shape_base import split


a1 = ['46,567', '46,980']
a2 = ['36,567', '46,567']


def get_points(lst):
    x1, y1 = lst[0].split(",")
    x2, y2 = lst[1].split(",")
    return int(x1), int(y1), int(x2), int(y2)

x1, y1, x2, y2 = get_points(a1)


if y1 == y2:
    pass
elif x1 == x2: 
    pass 

def calc_horizontal(x1, x2, y1):
    tmp_lst = []
    x_vals = range(min(x1, x2), (max(x1, x2) + 1))
    for x_val in x_vals:
        tmp_lst.append((x_val, y1))
    return tmp_lst    

calc_horizontal(46, 37, 12)

lst = []
point_dict = {}

f = open("input_day5.txt")
for newline in f:
    lst.append(newline.rstrip("\n").split(" -> "))

f.close()

print(val1)

split