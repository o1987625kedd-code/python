# exact_age = 25.85
# age = int(exact_age)
# print(f"使用者今年滿{age}歲")
# price_input = "199"
# discount = 0.85
# final_price = float(price_input) * discount
# print(f"打折後價格為：{final_price}")

# r,g,b = 255,165,0
# hex_color = f"#{hex(r)[2:]}{hex(g)[2:]}{hex(b)[2:]}"
# print(hex(r))
# print(hex(g))
# print(hex(b))
# print(hex_color)
# chmod_val = 493
# print(oct(chmod_val))
# total_seconds = 385
# minutes,seconds = divmod(total_seconds,60)
# print(f"總秒數 {total_seconds} 轉換為 {minutes} 分 {seconds} 秒")
# principal = 10000
# rate = 1.05
# years = 3
# total = principal * pow(rate, years)
# total = principal * pow(rate,years)
# print(f"3 年後本利和：{round(total)} 元")
# print(ord("A"))
# print(ord("a"))
# print(ord("0"))
# print(ord("台"))
# print(ord("😂"))

# print(chr(65))
# print(chr(97))
# print(chr(48))
# print(chr(21488))
# print(chr(128514))

# alphabet = [chr(i) for i in range(65, 91)]
# print(alphabet)

# char = "C"
# shift = 3
# new_char = chr(ord(char) + shift)
# print(f"{char}向後推{shift}位是:{new_char}")

#import math
# radius = 5.0
# circle_area = math.pi * (radius ** 2)
# print(f"半徑為{radius}的圓面積為: {circle_area:.2f}")
# a,b = 3.0,4.0
# c = math.sqrt(pow(a,2) +pow(b,2))
# print(f"直角三角形的斜邊長為: {c:.2f}")
# items = 23
# capacity_per_box = 10
# boxes_needed = math.ceil(items / capacity_per_box)
# print(f"需要的箱子數量為: {boxes_needed}")

# import math
# rent_hours = 50
# days = math.floor(rent_hours / 24)
# print(f"租用{rent_hours}小時，相當於{days}天")

# import math
# print(f"圓周率:{math.pi}")
# print(f"自然對數:{math.e}")

import math
val = -15
result = math.fabs(val)
print(f"{val} 的絕對值是: {result}")