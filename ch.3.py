pw= input('請輸入密碼  ')
if(pw=="1234"):
    print('歡迎光臨')
else:
    print('密碼錯誤')

score=int(input('請輸入成績  '))
if(score>=90):
    print('優等')
elif(score>=80):
    print("甲等")
elif(score>=70):
    print('乙等')
else:
    print('加油')

a= int(input('請輸入a的值 '))
b= int(input('請輸入b的值 '))
c= int(input('請輸入c的值 '))
if(a>b and a>c):
    print('最大值為'+str(a))
elif(b>a and b>c):
    print('最大值為'+str(b))
elif(c>a and c>b):
    print('最大值為'+str(c))
else:
    print('有一樣大的')

rain=input('今天會下雨嗎')
if (rain=="Y"or 'y'):
    print('出門要帶傘')
else:
    print('不下雨')

num=int(input('請輸入正整數  '))
if(num%2==0):
    print('偶數')
else:
    print('奇數')