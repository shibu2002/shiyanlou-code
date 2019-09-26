#!/usr/bin/env python3
print(50*'*')
for i in range (1,10):
    for j in range(1,10):
        print("{:5d}".format(i * j) , end=' ')
    print()
print(50*'*')
