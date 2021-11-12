from math import factorial as fact
from math import fabs

EPS = 1e-10

x = float(input("Value of x? "))
n = int(input("Value of n? "))
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







