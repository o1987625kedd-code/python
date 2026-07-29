# for x in 'Python':
#   print(x) # Python 以直行輸出
# print("ok")  
# # sum = 0
# # for x in range(1,11):
# #   sum += x
# # print(sum)

# for x in range(10,1,-2):
#   print(x)
# print("結束")
# i = 1
# sum = 0
# while (i <= 10):
#   sum += i
#   i += 1
# print(sum)
# import time
# i = 10
# while (i > 0):
#   print(i)
#   i -= 1
#   time.sleep(0.3)
# print("時間到！")

# for x in range(1, 6):
#     for y in range(1, 6 - x):
#         print(' ', end='')
#     for y in range(1, x + 1):
#         print('*', end = '')
#     print ( )
# print ( )

# i = 1
# sum = 0
# while(i <= 10):
#     sum += i
# i += 1
# print(sum)

# -*- coding: utf-8 -*-
for i in range(1,10):
    j = 1
    while 1:
        print(i, '*', j, '=', i*j, end='\t')
        j = j + 1
        if(j > 9):
            break
    print()
print()