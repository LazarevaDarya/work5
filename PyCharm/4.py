#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import factorial as fact
from math import fabs

EPS = 1e-10

x = float(input("x = "))
n = int(input("n = "))
k = 0
var = (x / 2) ** n
summa = float(0)

while True:
    prev_sum = summa
    temp = ((x ** 2) / 4) ** k
    summa = temp / (fact(k) * fact(k + n))
    k += 1
    if fabs(prev_sum - summa) < EPS:
        break

summa = var * summa

print(summa)







