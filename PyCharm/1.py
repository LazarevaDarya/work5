#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    m = int
    x = int(input("Value of x? "))
if x < 50:
     m = 30*x
elif x in range(50, 75):
     m = 50*x
elif x in range(75, 90):
     m = 65*x
else:
    m = (70*x)+20

print(m)
exit(1)
