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

unlikely = []
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
    cash = int(binary_searcher(i,1000000,900000))
    if cash > highest_cash:
        highest_cash = cash
r.sendline('2 ' + str(highest_cash))
print(r.recvline())
# g500000 = [] #greater than 500000
# l500000 = []
# g750000 = []
# g500000l750000 = []
# l250000 = []
# g250000l500000 = []
# for i in range(1,301):
#     r.sendline('1 ' + str(i) + ' ' + str(highest//2))
#     x = r.recvline()
#     if 'G' in x:
#         g500000.append(i)
#         print("greater than 5000000")
#     elif b'L' in x:
#         l500000.append(i)
#     elif b'E' in c:
#         unlikely.append(500000)
#
# print('g500000',g500000)
# for i in g500000:
#     r.sendline('1 ' + str(i) + ' ' + str((highest//2) +(highest//4)))
#     x = r.recvline()
#     if b'G' in x:
#         g750000.append(i)
#     elif b'L' in x:
#         g500000l750000.append(i)
#     elif b'E' in c:
#         unlikely.append(750000)
# # if len(g500000) == 0:
# #     for i in l500000:
# #         r.sendline('1 ' + str(i) + ' ' + str((highest//2) -(highest//4)))
# #         x = r.recvline()
# #         if b'G' in x:
# #             g250000l500000.append(i)
# #         elif b'L' in x:
# #             l250000.append(i)
# #         elif b'E' in c:
# #             unlikely.append(str(250000))
#
# greatest_list = g750000
# if len(g750000) == 0:
#     greatest_list = g500000l750000
#     # if len(g500000l750000) == 0:
#     #     greatest_list = g250000l500000
#     #     if len(g250000l500000) == 0:
#     #         greatest_list = g250000
#
# for i in greatest_list:
#     highest_cash = 0
#     cash = int(binary_searcher(i,1000000,750000,highest_cash))
#     if cash > highest_cash:
#         highest_cash = cash
# for i in unlikely:
#     if i > highest_cash:
#         highest_cash = i
#
# r.sendline('2 ' + str(highest_cash))
