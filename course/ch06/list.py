# # lst1 = [11,22,33,44,55,66,77,88,99]
# # print(lst1)
# # print(lst1[0])
# list2 = ["one","two","three","four","five","six"]
# list2[3] = "四"
# print(list2[3])
# print(list2)
# lst3 = [23,45,51,67,89,100]
# print(str(len(lst3)))
# lst4 = [11,22,33,44,55,66,77,88,99]
# for i in range(len(lst4)):
#   print(lst[i],end = " ")
# print()
# season = ["spring","summer","autumn","winter"]
# for item in season:
#   print(item,end = "*")
# arr = [True for x in range(6)]
# for item in arr:
#   print(item,end = " ")
  
  # 利用列表生成式建立一個長度為 5、裡面初始值都是 `0` 的列表，也就是 `[0, 0, 0, 0, 0]`。
# 利用列表生成式建立一個長度為 5、裡面初始值都是 `0` 的列表，也就是 `[0, 0, 0, 0, 0]`。
# lst = [0 for x in range(5)]
# print('請依序輸入5個整數...')
# for i in range(5):
#   print(f'輸入第 {i+1} 個元素內容：', end = '')
#   # 接收使用者在鍵盤輸入的文字，並將它轉成數字。
#   lst[i] = eval(input())
# # 找出最大值（演算法核心 
# max = lst[0] # 先假設第一個元素就是最大的
# for item in lst:
#   # 如果挑戰者 `item` 比目前的擂台主 `max` 還要大，就把擂台主換人，寫入 `max = item`。
#   if max < item : 
#      max = item
    
# print()
# print(f'最大值為 {max}')

# lst1 = [10,20,30,40,50]
# # print(str(num := len(lst1)))
# print(num := len(lst1))
# print(type(num))
# print(f"total = {sum(lst1)}")
# big = max(lst1)
# print(str(big))
# print(f"small = {min(lst1)}")

s1 = "電車月票"
s2 = 1280
print("項目：{0},金額：{1}".format(s1,s2))