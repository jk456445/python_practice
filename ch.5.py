score =[85, 79, 93]
print('國文成績: %d分' %(score[0]))
print('數學成績: %d分' %(score[1]))
print('英文成績: %d分' %(score[2]))

names=['林小虎', '王中森', '紹木淼']
print(names[-1])
for s in names:
    print(s, end=',')

subjects=['國文','數學','英文']
scores=[85,79,46]
for i in range(len(scores)):  #len(scores)出來的長度是3，range(len(scores))出來的東西會是0,1,2,所以i從0開始
    print('%s成績:%d分' %(subjects[i], scores[i]))

score=[]
total=inscore=0

while(inscore!=-1):
    inscore=int(input('請輸入學生成績 '))
    if(inscore!=-1):                    #要另外拉一個if出來寫，因為不這樣的話，當我輸入-1時，因為沒有經過while，所以還是會跑下面這兩行
        score.append(inscore)              #會被加進score裡面
        total+=inscore                      #這個可以先不寫，之後再寫一個for迴圈，像下面那樣

print('共有%d位學生' %(len(score)))              #for sc in score:       因為用for迴圈可以直接讀所有迴圈元素，方便
                                                #   total+=sc
                                                #   print(total)
print(total)

money=[]
total=0
for i in range(1,8):
    n=int(input('請輸入第%d天的存款:' %(i)))
    money.append(n)
    total+=n
print('存款總額:%d' %(total))

fruits=['香蕉','蘋果','橘子','鳳梨','西瓜']
while True:
    print('串列元素有:',fruits)
    fruit=input('請輸入要刪除的水果(enter結束):' )
    if(fruit==' '):
        break
    n=fruits.count(fruit)  #這裡不能用index()，因為要是輸入不在裡面的東西，會error
    if (n>0):
        fruits.remove(fruit)
    else:
        print(fruit,'不在串列中')
score=[]
while True:
    n=input('請輸入學生的成績:' )  #不能在這裡就改成int，不然下面那個空格是屬於string的就會error，所以下面再改
    if(n==''):
        break
    score.append(int(n))

score2=sorted(score,reverse=True)  #由大到小是True
print(score2)
