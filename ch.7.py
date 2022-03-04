def getarea(width, height):
    area= width*height
    return area
ret1= getarea(8,9)
print (ret1)

def ctof(c):
    f=c*1.8+32
    return f

inputc= float(input('請輸入攝氏溫度 '))
print('華氏溫度為:%5.1f度' %(ctof(inputc)))  #固定列印5個字元(含小數點)，小數後印一位

person= int(input('請輸入學生人數  '))
apple=int(input('請輸入蘋果個數  '))
ret = divmod(apple, person)         #出來的結果是商和餘數
print('每個學生可分得蘋果%d個' %(ret[0]))
print('蘋果剩餘%d個'%(ret[1]))

list2=[]
innum=0
while(innum!=-1):
    innum=int(input('請輸入電費(-1:結束):' ))
    if(innum!=-1):
        list2.append(innum)
print('共輸入%d個數'%(len(list2)))
print('最多電費為%d'%max(list2))
print('最少電費為%d'%min(list2))
print('電費由大到小排序為:{}'.format(sorted(list2,reverse=True)))

listname =['林大明','陳阿忠','張小英']
listchinese =[100,74,83]
listmath =[56,75,86]
listenglish =[95,94,90]
print('姓名     座號   國文   數學   英文')
for i in range(0,3):
    print(listname[i].ljust(5), str(i+1),
          str(listchinese[i]).rjust(7), str(listmath[i]).rjust(7),  #調成str才能改靠右or靠左，int是不能的
          str(listenglish[i]).rjust(7))

import random as r
while True:
    inkey=input('按任意建在按[enter]鍵擲骰子，直接按[enter]鍵結束:')
    if (len(inkey)>0):
        num= r.randint(1,6)
        print('你擲的骰子點數是{}'.format(num))
    else:
        print('遊戲結束')
        break

list3=r.sample(range(1,50),7)
special=list3.pop()
list3.sort()
print('本期大樂透中獎號碼為:')
for i in range(0,6):
    if i==5:
        print(str(list3[i]))        #跑到最後一個號碼時後面就不用逗點了，所以分開寫
    else:
        print(str(list3[i]),end=',')
print('本期大樂透特別號為:'+str(special))

import time as t

print(str(t.process_time()))  #現在已經沒有time.clock()這個函式了，變成time.process_time()，這個函式不會把sleep經過的時間算進去
week=['一','二','三','四','五','六','日']
light=['無日光節約時間','有日光節約時間']
time1= t.localtime()
show= '現在時刻:中華民國'+str(int(time1.tm_year)-1911)+'年'+str(time1.tm_mon)+'月'+str(time1.tm_mday)+'日'
show+=str(time1.tm_hour)+'點'+str(time1.tm_min)+'分'+str(time1.tm_sec)+'秒  星期  '+ week[int(time1.tm_wday)]+'\n'
show+="今天是今年的第"+str(time1.tm_yday)+'天，這裡'+light[int(time1.tm_isdst)]
print(show)

