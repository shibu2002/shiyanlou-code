#!/usr/bin/env python3
wholenum = int(input('please input sticker number'))
while wholenum > 1:
    print('there are {} sticks'.format(wholenum))
    usersel = int (input('please select sticks num 1-4 :'))
    computersel = (wholenum - usersel) % 5 -1
    if computersel == -1:
        computersel = 4
    elif computersel == 0:
        computersel = 1
    wholenum = wholenum - usersel - computersel
    print('there are {} left, computer take {} away'.format(wholenum,computersel))
if wholenum == 1:
    print('you lose')
else:
    print('you win')

