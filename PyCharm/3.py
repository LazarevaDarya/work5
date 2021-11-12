#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    m = int
    n = int(input("Value of n? "))
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            print(i)




