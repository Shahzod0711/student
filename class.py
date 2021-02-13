# class Uy:
#     def __init__(self,turi,xonasi,rangi,balandligi):
#         self.turi = turi
#         self.xonasi = xonasi
#         self.rangi = rangi
#         self.balandligi = balandligi
#     def __str__(self):
#         return "Turi:\t"+self.turi + "Xonasi:\t"+self.xonasi + "Rangi:\t"+self.rangi + "Balandligi:\t"+self.balandligi
    
# Uylist = []
# while True:
#     print("1-Uyni qo'shish\n2-ro'yxatni chiqarish\n3-turi bo'yicha tartiblash\n4-xonasi bo'yicha tartiblash\nq-quit")
#     cmd = input()
#     if cmd == "1":
#         turi = input("TURni kiriting:")
#         Xonasi = input("Xonasini kiriting:")
#         Rangini = input("Rangini kiriting:")
#         Balandligini = input("Balandligini kiriting:")

#         home = Uy(turi,Xonasi,Rangini,Balandligini)
#         Uylist.append(home)
#     elif cmd == "2":
#         print("____UY RO'YXATI___")
#         for home in Uylist:
#             print(home)
#         print("_____________________________________")
#     elif cmd == "3":
#         sortedList = Uylist
#         sortedList.sort(key=lambda x:x.kurs)
#         for i in sortedList:
#             print(i)

#     elif cmd == "4":
#         sortedList = Uylist
#         sortedList.sort(key=lambda x:x.age)
#         for i in sortedList:
#             print(i)
#     elif cmd == "q":
#         break

#2

# class Duck: 
#     def __init__(self,value,value2):
#         self._v = value
#         self._v2 = value2

#     def quack(self):
#         print("Quackkkkk",self._v,self._v2)
#     def walk(self):
#         print("Walks like a duck!",self._v,self._v2)
# def main():
#     donald = Duck(2312321,61565165)
#     donald.quack()
#     donald.walk()
# if __name__ == "__main__":main()

#3

# class Duck:
#     def __init__(self,**kwargs):#kwargs katta elementlar
#         self.properties = kwargs
#     def quack(self):
#         print("Quackkkk")
#     def walk(self):
#         print("Walks like a duck")
#     def get_properties(self):
#         return self.properties
#     def get_properties(self,key):
#         return self.properties.get(key,None)
#     @property
#     def color(self):#get dostup olish(kalitni olish)
#         return self.properties.get('color',None)
#     @color.setter#qiymat kiritish imkoniyatini ochish
#     def color(self,c):
#         self.properties['color'] = c 
#     @color.deleter
#     def color(self):
#         del self.properties['color']
# def main():
#     donald = Duck()
#     donald.color = 'red'
#     print(donald.color)
# if __name__ == "__main__":main()

#4

# class inclusive_range:#for range (start,stop,step)
#     def __init__(self,*args):
#         numargs = len(args)
#         if numargs <1:raise TypeError("We expect arguments")
#         elif numargs == 1: #stop 25
#             self.stop = args[0] #for i in range(10): 1+1+1+1+
#             self.start = 0
#             self.step = 1
#         elif numargs == 2: #for i in range(start(0),stop(15)):
#             (self.start,self.stop) = args
#             self.step = 1
#         elif numargs == 3: # for i in range(start(0),stop(15),step(1))
#             (self.start,self.stop,self.step) = args
#         else: raise TypeError("Expected at most 3 arguments, got{}".format(numargs))

#     def __iter__(self):
#         i = self.start
#         while i <= self.stop:
#             yield i
#             i += self.step #2+2+2+2+2
# def main():
#     o = inclusive_range(5,21,2)
#     for i in o: print(i) #for i in range(5,21,1):print(i)

# if __name__ == "__main__":main()

#5

#inheritance class
# class Animal:
#     def talk(self):print("Hey I talk")
#     def walk(self):print("Hey I walk")
#     def clothes(self):print("Hey I have nice clothes")

# class Duck(Animal):
#     def quack(self):
#         print("Quack")
#     def walk(self):
#         super().walk()
#         print("Walks like a duck")
# class Dog(Animal):
#     def clothes(self):print("I have a brown and white fur")

# def main():
#     donald = Duck()
#     donald.quack()
#     donald.walk()#overrides 
#     donald.clothes()

#     fido = Dog()
#     fido.walk()
#     fido.clothes()#overrides
# if __name__ == "__main__":main()

#6

#polimorfizm
# class Duck:
#     def quack(self):print("Quackkkk")
#     def walk(self):print("Walks like a duck")
#     def bark(self):print("The duck can not bark")
#     def fur(self):print("The duck has feathers")
# class Dog:
#     def bark(self):print("Woof!")
#     def fur(self):print("The dog has brown and white fur")
#     def walk(self):print("Walks like a dog")
#     def quack(self):print("The dog can not quackkk")
# def main():
#     donald = Duck()
#     fido = Dog()
#     in_the_forest(donald)
#     in_the_pond(fido)

# def in_the_forest(cat):
#     cat.bark()
#     cat.fur()
# def in_the_pond(duck):
#     duck.quack()
#     duck.walk() 

# if __name__ == "__main__":main()

#7

 #class objectdata
# class Duck:
#     def __init__(self,**kwargs):
#         self.variables = kwargs
#     def set_variable(self,k,v):
#         self.variables[k]=v
#     def get_variables(self,k):
#         return self.variables.get(k,None)
    
# def main():
#     donald = Duck(feet = 15151,arm = 15165165)
#     donald.set_variable('color','blue')
#     print(donald.get_variables('feet'))
#     print(donald.get_variables('color'))
#     print(donald.get_variables('arm'))
# if __name__ == "__main__":main()