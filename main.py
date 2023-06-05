# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings

import random
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


lista_x= []
lista_y= []

num = 5
max = 10
min = 0

A = (max-min)*(max-min)
print(A)

print('lista per le y')

for x in range(num):
    Cosa=(random.uniform(min,max))
    lista_y.append(Cosa)
    print(Cosa)

print('lista per le x')

for x in range(num):
    Coso=(random.uniform(min,max))
    lista_x.append(Coso)
    print(Coso)

np.savetxt("X.csv", lista_x, delimiter=", ", fmt="%s")
np.savetxt("Y.csv", lista_y, delimiter=", ", fmt="%s")



#plt.hist(mylist, bins=100)
































