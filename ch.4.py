n = int(input('請輸入正整數  '))
sum = 0
for i in range(1, n+1):
    sum += i
print("1到%d 的整數和為 %d" % ( n , sum))

a=int(input('請輸入正整數  '))
for i in range(0,a+1,2):
    print(i,end='\n')

for i in range(1, 10):
    for j in range(1, 10):
        product= i*j
        print('%d *%d=%2d' % (i,j,product), end=' ')
    print()

a=int(input('請輸入正整數  '))
for i in range(1,a+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

a= int(input('請輸入正整數 '))
b=int(input('請輸入正整數  '))
x=a*b+1
for i in range(1,x):
    if(i%a==0 and i%b==0):
        break
print('%d和 %d 的最小公倍數=%d' %(a,b,i))  #要放在for迴圈外面，如果放裡面，表示只要不合的就不會break，但會印出這行

c= int(input('請輸入正整數 '))
for i in range(1,c+1):
    if (i%5==0):
        continue  #跑到continue的話，就直接執行下一個數，不執行下面還沒做完的print
    print(i, end=',')

f=int(input('請輸入正整數 '))
total=d=1
while(d<(f+1)):
    total*=d
    d+=1
print(total)

e=int(input('請輸入正整數 '))
i=0
while(i<=e):
    if(i%2==0):
        print(i)
    i+=1

count = 0
inputs = int(input("請輸入正整數n的值：\n"))
print('顯示結果:', end='')
while True:
    if count % 2 == 0 and count > 1:
        print(count, ' ', end='')
    if count == inputs:
        break
    count += 1