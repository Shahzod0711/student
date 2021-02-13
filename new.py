# a=int (input("a="))
# s=a**2
# print( "yuasi S=",s) 

# import random
# N = random.randrange(10)+1
# # K = random.uniform(-10, 10)
# K = random.randrange(-10, 10)

# print('K = ', K)
# print('N = ', N)
# for i in range(0, N):
#     print(i+1," : ",K)
#3
# import random
# import math
# def get_mean(x,y,result):
#     result['amean']=(x+y)/2
#     result['gmean']=math.sqrt(x*y)
#     return

# r = {'amean':'None','gmean':'None'}
# a = random.randrange(0,10)
# b = random.randrange(0,10)
# c = random.randrange(0,10)
# d = random.randrange(0,10)

# print('a:',a,'b:',b,'c:',c,'d:',d)
# get_mean(a,b,r)

# print('amean:',r['amean'])
# print('gmean:',r['gmean'])

# get_mean(a,c,r)

# print('amean:',r['amean'])
# print('gmean:',r['gmean'])

# get_mean(a,d,r)

# print('amean:',r['amean'])
# print('gmean:',r['gmean'])
#4
#  import random
# import math
# def get_triangle(a,result):
#     result['p'] = 3*a
#     result['s']=math.sqrt(3)/4*a*a
#     return
# r = {'p':'None','s':'None'}
# for i in range(3):
#     a = random.randrange(1,10)
#     print('a:',a)
#     get_triangle(a,r)
#     print('P:',r['p'])
#     print('S:',r['s'])
#     print()
#5
# import random
# def get_rectps(x1,x2,y1,y2,result):
#     a = abs(x1-x2)
#     b = abs(y1-y2)
#     print(a," ",b)
#     result['p']=2*(a+b)
#     result['s']=a*b
#     return

# x1,x2 = random.sample(range(-10,10),2)
# y1,y2 = random.sample(range(-10,10),2)
# print(x1," ",x2," ",y1," ",y2)
# r = {'p':'None','s':'None'}
# get_rectps(x1,x2,y1,y2,r)
# print('p:',r['p'])
# print('s:',r['s'])
#6
# import random
# def get_digitcountsum(k,result):
#     s = str(k)
#     n = len(s)
#     _sum = 0
#     for i in range(n):
#         _sum += int(s[i])# 165
#     result['c']=n
#     result['s']=_sum

# r = {'c':'None','s':'None'}
# for i in range(5):
#     k = random.randrange(1,10000000000000000)
#     print('Son:',i+1,":",k)
#     get_digitcountsum(k,r)
#     print("Sonlar soni:",r['c'])
#     print("sonlar yig'indisi:",r['s'])
#     print()
#7
# import random
# def get_invertDigits(k):
#     s = str(k['k'])
#     s_new = s[::-1]
#     k['k']=int(s_new)

# r = {'k':None}
# for i in range(5):
#     r['k']=random.randrange(1,1000000000)
#     print('son',i+1,":",r['k'])
#     get_invertDigits(r)
#     print("O'zgargan son:",r['k'])
#     print()
#8
# import random
# def addRightDigit(d,k):
#     k['k']=d+k['k']*10

# r = {'k':None}
# r['k']=random.randrange(1,100000)
# print("K sonim:",r['k'])
# for i in range(3):
#     d = random.randrange(1,10)
#     print("D sonim:",i+1,":",d)
#     addRightDigit(d,r)
#     print("k o'zgargani:",r['k'])
#     print()
#9
class Uy:
    def __init__(self,turi,xonasi,rangi,balandligi):
        self.Turi = turi
        self.Xonasi = xonasi
        self.Rangi = rangi
        self.Balandligi = balandligi
    def str(self):
        return "Turi:\t"+self.turi + "Xonasi:\t"+self.xonasi + "Rangi:\t"+self.rangi + "Balandligi:\t"+self.balandligi
    
Uylist = []
while True:
    print("1-Uyni qo'shish\n2-ro'yxatni chiqarish\n3-turi bo'yicha tartiblash\n4-xonasi bo'yicha tartiblash\nq-quit")
    cmd = input()
    if cmd == "1":
        turi = input("Turni kiriting:")
        Xonasi = input("Xonasini kiriting:")
        Rangini = input("Rangini kiriting:")
        Balandligini = input("Balandligini kiriting:")

        home = Uy(turi,Xonasi,Rangini,Balandligini)
        Uylist.append(home)
    elif cmd == "2":
        print("____UY RO'YXATI___")
        for home in Uylist:
            print(home)
        print("_____________________________________")
    elif cmd == "3":
        sortedList = Uylist
        sortedList.sort(key=lambda x:x.kurs)
        for i in sortedList:
            print(i)

    elif cmd == "4":
        sortedList = Uylist
        sortedList.sort(key=lambda x:x.age)
        for i in sortedList:
            print(i)
    elif cmd == "q":
        break