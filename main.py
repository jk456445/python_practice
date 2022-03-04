
str1 = '{小明說"你好"}'
print(str1)
str2 ='大家好\n歡迎光臨'       #\n是換行 所以歡迎光臨跑到下一列
print(str2)

print(type(56))  #用TYPE可以知道打在()裡面的資料型態是什麼，所以打56就會出來int
score=30
print("小明的成績為"+str(score))  #用str()就可以把原本是int的score轉換成字串，才可以和前面的字串加起來輸出，同理，也可以用int()和float()

print(100, '多吃水果', 60, sep='-', end='@')  #sep是分隔符號, end是結束字元,預設是換下一列，所以我如果改成@，下一次print就會印在@後面
print('試試')

name, age="阿呆",24
print("{}的成績為  {}{}".format(name, score,age))  #print(字串.format(參數列))，用{}表示參數的位置，照參數裡面的順序顯示出來

print("姓名 座號 國文 數學 英文" )
print("%3s %2d %2d %2d %2d"  %('林大名', 1 , 100, 87, 79))
print("%3s %2d %2d %2d %2d" %("張阿忠", 2, 74, 88, 100))
print("%3s %2d %2d %2d %2d"  %("張小花", 3, 87, 80, 100))

chinese= int(input("請輸入國文成績 "))
math= int(input('請輸入數學成績 '))
english= int(input('請輸入英文成績 '))
total = chinese+math+english
print("成績總分為"+str(total))

up=int(input('請輸入梯形上底 '))
down= int(input('請輸入梯形下底  '))
high= int(input('請輸入梯形高 '))
area=(up+down)*high/2
print(area)

phone=int(input('請輸入手機金額  '))
now=50000
after=now-phone
print(after)

mile=int(input('請輸入搭乘的公里數(整數)  '))
money=70+30*(mile-1)
print(money)

