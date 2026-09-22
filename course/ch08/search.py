# 建立一個名為 datas 的字典（Dictionary），儲存商品資料
# Key 為貨號（字串），Value 為包含 [品名, 售價] 的串列（List）
datas = {'A001':['汽水',25],
        'A005':['公主麵',10],
        'A006':['口香糖',8],
        'A003':['冰棒',20]}
# 提示使用者輸入貨號，並將輸入的字串儲存至變數 num 中
num=input('請輸入貨號：')
# 檢查使用者輸入的貨號 (num) 是否「不存在」於字典 (datas) 的 Key
if num not in datas:
    # 若貨號不存在，印出提示訊息告知使用者該貨號不存在
    print(f'貨號：{num} 不存在')
    # 提示使用者輸入品名，將輸入的字串儲存至變數 name
    name=input('請輸入品名：')
    # 提示使用者輸入售價，並使用 int() 將輸入的字串強制轉換為整數後儲存至變數 money
    money=int(input('請輸入售價：'))
    # 將新貨號作為 Key，[品名, 售價] 串列作為 Value，新增至 datas 字典中
    datas[num]=[name,money]
# 使用字典的 .get() 方法取得指定貨號 (num) 對應的 Value（即 [品名, 售價] 串列），並賦予變數 d
d = datas.get(num)
print(f'貨號：{num} 品名：{d[0]} 售價：{d[1]}元')