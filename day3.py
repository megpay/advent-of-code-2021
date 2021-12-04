import numpy as np

def calc_gamma_epsilon(lst, i):
    gamma = []
    epsilon = []
    for elem in lst:
        if elem > i/2:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
    return(''.join(map(str, gamma)), ''.join(map(str, epsilon)))


f = open("inputday3.txt")
i = 0
newlst = lst = []
for newline in f:
    lst = [int(x) for x in str.rstrip(newline)]
    if newlst == []:
        newlst = [0] * len(lst)
    newlst = [lst[i]+newlst[i] for i in range(len(lst))]
    i += 1

f.close()

g, e = calc_gamma_epsilon(newlst, 1000)
int(g, 2) * int(e, 2)
