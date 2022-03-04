dict1 = {'A':'內向穩重','B':'外向樂觀','O':'堅強自信','AB':'聰明自然'}
name=input('請輸入血型: ')
blood=dict1.get(name)
if (blood==None):
    print('沒有'+name+'血型')
else:
    print(name+'血型的個性為'+str(blood))

dict2={'林小明':85,'曾山水':93,'鄭美麗':67}
name=input('請輸入學生姓名:')
a=dict2.get(name)
if a==None:
    score=int(input('請輸入學生分數:' ))
    dict2[name]=score
    print('字典內容:'+ str(dict2))
else:
    print(name+'的成績為'+str(a))