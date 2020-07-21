import math
from pwn import *

def binary_searcher(i,up,down):
    while True:
        mid = (up+down)//2
        r.sendline('1 '+ str(i) + ' ' + str(mid))
        x = r.recvline()
        if b'G' in x:
            down = mid
        elif b'L' in x:
            up = mid
        elif b'E' in x:
            return str(mid)

r = remote('chall.csivit.com',30721,level='debug')
highest = 1000000
list1 = []
for i in range(1,301):
    r.sendline('1 ' + str(i) + ' ' + str(900000))
    x = r.recvline()
    if 'G' in x:
        list1.append(i)
    elif b'L' in x:
        pass
    elif b'E' in c:
        pass
print(list1,len(list1))
highest_cash = 0
for i in list1:
    cash = int(cash_finder(i,1000000,900000))
    if cash > highest_cash:
        highest_cash = cash
r.sendline('2 ' + str(highest_cash))
print(r.recvline())

