class Uy:
    def __init__(self,turi,xonasi,rangi,balandligi):
        self.turi = turi
        self.xonasi = xonasi
        self.rangi = rangi
        self.balandligi = balandligi
    def __str__(self):
        return "Turi:\t"+self.turi + "Xonasi:\t"+self.xonasi + "Rangi:\t"+self.rangi + "Balandligi:\t"+self.balandligi
    
Uylist = []
while True:
    print("1-Uyni qo'shish\n2-ro'yxatni chiqarish\n3-turi bo'yicha tartiblash\n4-xonasi bo'yicha tartiblash\nq-quit")
    cmd = input()
    if cmd == "1":
        turi = input("TURni kiriting:")
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