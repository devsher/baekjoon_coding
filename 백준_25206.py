# -*- coding: utf-8 -*-
"""백준_25206

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YzAPmt0MaMXD2z3gwxyhsWuQUy6YwVj_
"""

credit = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

sum1 = 0
sum2 = 0
for _ in range(20):
    a, b, c = input().split()
    b = float(b)
    if c != 'P':
        sum1 += b
        sum2 += b * credit[c]

print("%.6f" % (sum2 / sum1))