#!/usr/bin/env python3
while True:
    inputnum = input('please input an integrate number')
    if int(inputnum) < 0:
        continue
    elif int(inputnum) > 0:
        print('square is {} '.format(int(inputnum) ** 2))
    else:
        break


