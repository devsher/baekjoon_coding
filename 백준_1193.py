# -*- coding: utf-8 -*-
"""백준.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bfNTxyq45rEnXbay5JbTv4gYzSQWD7va
"""

#백준 1193
n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

diff = end - n
if line%2 == 0: #짝수 라인 일때
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d"%(top,bottom))