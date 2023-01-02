class Fruit:
    def __init__(self,name = "Banana", colour = "żółty"):
        self.name = name
        self.colour = colour
    def present(self):
        print("Ten owoc to", self.name)
        print("A jego kolor to",self.colour)


def mainFruit():
    fruit1 = Fruit("banana", "żółty")
    fruit2 = Fruit()
    print(fruit1.present())
    print(fruit2.present())

class Book:
    def __init__(self, title, pageNumber, author, releaseDate, owner):
        self.title = title
        self.pageNumber = pageNumber
        self.author = author
        self.releaseDate = releaseDate
        self.owner = owner

    def introduce(self):
        print("\rTytuł: ",self.title, "\r\n Autor: ",self.author, "\r\n Data wydania", self.releaseDate, "\r\n Ilość stron: ", self.pageNumber,"\r\n Właściciel: ", self.owner)
    def ownerChange(self, newOwner):
        self.owner = newOwner

def bookAppender():

    book1 = Book("1984", 200,"George Orwell", "2020.04.20", "Kasia Fox")
    book2 = Book("Granica", 500,"Kapka Kassabova", "2019.04.20", "Kasia Fox")
    book3 = Book("Legenda o świętym pijaku i inne opowiadania", 250,"Joseph Roth", "2016.04.20", "Kasia Fox")
    book4 = Book("Nędznicy", 1000,"Wiotr Hugo", "2020.05.20", "Kasia Fox")
    list = [book1,book2,book3,book4]

    for i in list:
        print(i.title)


class Jednoslad:
    def __init__(self, type, engCap, brand, mileage):
        self.type = type
        self.engCap = engCap
        self.brand = brand
        self.mileage = mileage
    def go(self):
        self.mileage += 1
    def startEngine(self):
        print(self.brand,"Uruchamia swój silnik", self.engCap, "bruuuum")
    def giveMileage(self):
        print("Mój przebieg to", self.mileage)

class Skuter(Jednoslad):
    pass

class Motor(Jednoslad):
    def __init__(self, engCap, maxSpeed):
        super().__init__("motocykl", engCap, brand=None, mileage=None)
        self.maxSpeed = maxSpeed

    def winterIsComing(self):
        print("Stoję całą zimę, bo nikt mną nie jeździ.")
        print("Moja maksymalna prędkość to", self.maxSpeed)
        print("A moja pojemność silnika to ", self.engCap)


class samochód:

    def __init__(self):

        self.__silnik = False
        self.__bieg = 0
        self.__prędkość = 0

    def uruchom(self):
        self.__silnik = True

    def wyłącz(self):
        self.__silnik = False

    def __biegNastępny(self):
        if self.__bieg <= 6: self.__bieg += 1; print(self.__bieg)

    def __biegPoprzedni(self):
        if self.__bieg >= 0: self.__bieg -= 1; print(self.__bieg)

    def przyspiesz(self):
        if self.__silnik == True and self.__bieg > 0: self.__prędkość += 10; print(self.__prędkość)
        self.__biegNastępny()

    def hamuj(self):
        if self.__prędkość >= 10:
            self.__prędkość -= 10
        else:
            self.__prędkość = 0
        self.__biegPoprzedni()
class Automat(samochód):
    def przyspiesz(self):
        self.biegNastępny()
        pass
    def hamuj(self):
        self.biegPoprzedni()
        pass

class Budynek():
    def __init__(self):
        self.__liczbaOsob = 0
    def entryBuiling(self):
        self.__liczbaOsob += 1
    def exitBuilding(self):
        if self.__liczbaOsob > 0 :
            self.__liczbaOsob -= 1
    def ifEmpty(self):
        return self.__liczbaOsob <0

