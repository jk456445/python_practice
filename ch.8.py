def disp_data():            #不輸入參數值，只要召喚這個函式，就是印datas出來
    for item in datas:
        print(item, end='')

datas=[3,5,2,1]
print('排序前:',end='')
disp_data()
n= len(datas)-1             #會印出3

for i in range(0,n):         #i是0,1,2，這樣共會跑3輪
    for j in range(0,n-i):   #當i=0，j=0,1,2，因為會是0 vs 1，1 vs 2， 2 vs 3，i每+1，j迴圈要處理的元素就少一個
        print('i=%d, j=%d'%(i,j))
        if(datas[j]>datas[j+1]):
            print('%d,%d互換後'%(datas[j],datas[j+1]), end=':')
            datas[j], datas[j+1]=datas[j+1], datas[j]       #python的可以直接這樣互換，不用另外弄一個變數給他放
            print(datas)
print('排序後:',end='')
disp_data()

num=[256,731,943,389,142,645,829,945]
name=['小明','小美','小和','小乖','小寶','小該','曉培','小釵']
no= int(input('請輸入中獎者編號: '))

Isfound=False           #旗標，先預設還沒找到，所以是False
for i in range(len(name)):
    if(num[i]== no):
        Isfound=True
        break
if (Isfound==True):
    print('中獎者的姓名為: '+name[i])
else:
    print('無此中獎號碼')
print('共比對%d次'%(i+1))       #i要+1，因為i是從0開始的

num=[256,731,943,389,142,645,829,945,371,418]
name2=['小虎','中森','木淼','大同','子孔','美麗','溫柔','來福','天良','水品']

n=len(num)-1
Isfound= False
min=0
max=n
c=0     #計算比對次數

for i in range(0,n):            #先把順序排好
    for j in range(n-i):
        if (num[j]>num[j+1]):
            num[j], num[j+1]=num[j+1], num[j]       #兩數互換
            name2[j], name2[j+1]=name2[j+1], name2[j]#姓名互換

no=int(input('請輸入中獎者的編號  '))
while(min<=max):
    mid=int((min+max)/2)
    c+=1
    if(num[mid]==no):
        Isfound=True
        break
    if(num[mid]>no):        #中間值大於輸入值，用小的那半邊繼續比
        max=mid-1
    else:
        min=mid+1           #中間值小於輸入值，用大的那半邊繼續比
if(Isfound==True):
    print('中獎者的姓名為:'+name2[mid])
else:
    print('無此中獎號碼')
print('共比對%d次'%(c))

