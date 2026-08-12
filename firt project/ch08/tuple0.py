# 不加逗號「也 OK」，通常是因為寫成 x = (25) 時程式不會報錯，但此時它的型態已經變成一般的整數（int），而不是元組（tuple）。
# 在 Python 中，真正決定一個物件是不是元組的，是「逗號 ','」，而不是「括號 ()」
tuple1 = 25, 
tuple2 = (25,)
tuple3 = (25)
tuple4 = 25
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(type(tuple4)) 