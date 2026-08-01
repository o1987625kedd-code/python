# lst1 = [10,20,30,40]
# print(str(tf := 40 in lst1))

# st1 = '人之初@性本善@性相近@習相遠'
# arr1 = st1.split('@')
# print(arr1[0]) # 印出 ['人之初', '性本善', '性相近', '習相遠']

# arr2 = ['苟不教', '性乃遷', '教之道', '貴以專']
# # 連結字元為一個空格。連結字元會成為連結字元的一部分。
# st2 = ' '.join(arr2)
# print(type(st2))            # 印出 苟不教 性乃遷 教之道 貴以專

# lst = []
# # 計算輸入字元總長度
# count = eval(input('請輸入lst串列的元素數量：'))
# print('請依序填入各元素的內容...') 
# # 會產生一個從 0 開始、長度為 count 的數字序列
# for i in range(count):
#     num = eval(input())
#     lst.append(num)
#     print(f'輸入第 {i+1} 個元素內容：' , end = '')

   
# print('lst串列的元素內容：')
# for x in lst:
#     print(x, end = ' ')

# score = [72,98,86,76,63]
# score.sort()
# print(score)

# animal =["dog","cat","monkey","fox","tiger"]
# animal.reverse()
# print(animal)

# animal = ['dog','cat','monkey','fox','tiger']
# data = sorted(animal, reverse = False)
# print(f'animal = {animal}') # animal=['dog','cat','monkey','fox','tiger']
# print(f'data = {data}')    # data = ['cat','dog','fox','monkey','tiger']

# A = [0 for x in range(2)]
# print(A) 

# arr = [A for y in range(4)]
# print(arr)
no = [1,2,3,4]                                           # 編號
score = [[87,64,88],[93,72,86],[80,88,89],[79,91,90]]    # 成績   
print('編號   語文   數理   智力   總分')
print('================================')
# 迴圈跑 len(no)=4 次， i =0, 1, 2, 3
for i in range(len(no)):
    # 印出 編號 1, 2, 3, 4 (2 位數字)
    print(f'{no[i]:2d}', end = '    ')
    hSum = 0
    # j = 0, 1, 2, 3
    # 計算每一 row 加總成績 for 每一編號學生
    for j in range(len(score[i])):
        print(f'{score[i][j]:3d}', end = '    ')
        hSum += score[i][j]
    print(f'{hSum:3d}')
 
print('平均', end = '   ')
# j = 0, 1, 2
for j in range(3):
    vSum = 0
    # i = 0, 1, 2    j = 0
    # i = 0, 1, 2    j = 1
    # i = 0, 1, 2    j = 2     
    for i in range(len(no)):
        vSum += score[i][j]
    # 平均 = ([0][0] + [1][0] + [2][0]) / 3 
    # 平均 = ([0][1] + [1][1] + [2][1]) / 3 
    # 平均 = ([0][2] + [1][2] + [2][2]) / 3 
    # 平均 = ([0][3] + [1][3] + [2][3]) / 3     
    print(f'{vSum/len(no):4.1f}', end = '   ')