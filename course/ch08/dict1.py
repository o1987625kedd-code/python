dict1 = {"一月":"正月","二月":"花月","三月":"梅月"}
print(dict1["三月"])
dict1["一月"] = "元月"
print(dict1)
del dict1["一月"]
print(dict1)
dict1['一月'] = '正月' 
print(dict1)
print('1月' in dict1)
dict1 = dict((("一月","正月"),("二月","花月"),("三月","梅月")))
print(dict1)
dict2 = dict.fromkeys(("四月","五月"))
print(dict2)
dict2 = dict.fromkeys(["六月","七月"],"夏月")
print(dict2.keys())
print(dict2.values())
print(dict2.get('三月')) 
print(dict2.setdefault('一月', '梅月'))
print(dict2)
print(dict2.setdefault('一月', '寒月'))
print(dict2)
print(dict2.setdefault('九月', '臘月'))
print(dict2)
print(dict2.setdefault('九月', '臘月'))
print(dict2)
print(dict1.pop('10 月', 'NONE')) # NONE
print(dict2.pop('一月'))
print(dict2)
kiki = dict2.pop('六月')
print(kiki)
print(dict2)
doc = dict2.popitem()
print(doc)
print(dict2)
dict3 = {"一月":"正月","二月":"花月","三月":"梅月"}
dict2.update(dict3)
print(dict2)
dict4 = {"八月":"暑假","十月":"國慶","七月":"西瓜"}
dict2.update(dict4)
print(dict2)
dict2.clear()
print(dict2) # 輸出結果 {}