# -*- coding: utf-8 -*-
"""2587

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f2pz5v-aLhJf1BZGvFIeqp8jLSdekPAq
"""

x = []
for i in range(5):
    x.append(int(input()))
x.sort()
print(int(sum(x)/5))
print(x[2])