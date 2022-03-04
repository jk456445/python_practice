import requests
content="'hello python" \
        "中文字測試" \
        "welcome\n'"

#放在內容裡面的要用"'......'"包起來
f= open('file1.txt','w')
f.write(content)
f=open('file1.txt','r')
for line in f:
        print(line,end='')
f.close()

try:
        a=int(input('請輸入第一個整數:'))
        b=int(input('請輸入第二個整數:'))
        r=a%b
        print('r=',r)
except ValueError:
        print('發生輸入非數值的錯誤')
except Exception as e:
        print('發生',e,'的錯誤，包含分母為0的錯誤')
finally:
        print('一定會執行的程式區塊')


