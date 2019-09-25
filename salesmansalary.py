#!/usr/bin/env python3
camnum = int(input('please input camera number'))
price1 = int(input('please input camera price'))
bonus = 1500 + camnum * 200 + camnum * price1 * 0.02
print('your salary is {:10.2f}'.format(bonus))
