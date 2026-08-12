from random import randint
pc = set()
while len(pc) < 2:
    pc.add(randint(1, 7))
print(f'電腦的號碼是：{pc}，請輸入兩個 1~7 的號碼，總共有三次機會')
count = 3
while count :
    your = set()
    while len(your) < 2:
      x = int(input(f"請輸入第{len(your)}個號碼:"))
      if x <= 7 and x >0:
        your.add(x)
    if pc == your:
        print(f'恭喜你猜對了，電腦的號碼是：{pc}')
        break
    print(f'你輸入的號碼是：{your}，電腦的號碼是：{pc}，你還有 {count-1} 次機會')
    count -= 1
    