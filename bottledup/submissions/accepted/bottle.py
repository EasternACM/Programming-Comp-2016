#!/usr/bin/python3

line = input()
splitLine = line.split(' ')
s = int(splitLine[0])
v1 = int(splitLine[1])
v2 = int(splitLine[2])

n1 = s // v1
n2 = (s % v1) // v2


while n1 >= 0 and n1 * v1 + n2 * v2 != s:
  n1 -= 1
  n2 = (s - n1 * v1) // v2

if n1 < 0:
  print("Impossible")
else:
  print(n1,n2)

