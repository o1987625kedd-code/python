t1 = (10,20,30)
print(sum(t1,40))
print(max(t1))
print(min(t1))
list1 = [10,20,30]
print(tuple(list1))
tuple1 = (10,20,30)
print(list(tuple1))
print(len(tuple1))
print(tuple1.count(30))
tuple1 = (30,20,50,10,60,70,80,90,90)
print(sorted(tuple1))
tuple2 = ("東","南","西")
print(tuple2)
east,south,west = tuple2
print(south)
# del(tuple2)
# print(tuple2)  # NameError: name 'tuple2' is not defined
list1 = list(tuple1)
list1.append('東北')
print(list1) # ['東', '南', '西', '北', '東北']

tuple1 = tuple(list1) 
print(tuple1) # ('東', '南', '西', '北', '東北')
print(tuple1[0]) # 東
print('東北' in tuple1) # True
print("東南" in tuple1)
for t in tuple1:
  print(t, end="")