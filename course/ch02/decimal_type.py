import decimal
f1 , f2 = 10.0,3.0
d1 = decimal.Decimal(10)
print(type(d1))

import decimal

f = 0.1  # 這裡的 0.1 已經先被電腦二進位污染了
d = decimal.Decimal(f)
print(d)  # 輸出依然會是一長串失真的數字：0.10000000000000000555...