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

bookAppender()



