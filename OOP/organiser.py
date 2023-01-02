from atribiutes import Note, VisitingCard
class Organiser():
    __database = []
    def addNote(self):
        title = input("Podaj tytuł notatki")
        content = input("Podaj Treść notatki: ")
        newNote = Note(title, content)
        self.__database.append(newNote)
    def addVisitCard(self):
        firstName = input("Podaj imię do wizytówki: ")
        lastName = input("Podaj nazwisko do wizytówki: ")
        telephone = input("Podaj telefon do wizytówki: ")
        newCard = VisitingCard(firstName, lastName, telephone)
        self.__database.append(newCard)
    def showNotes(self):
        for i in self.__database:
            if i.type == "notatka":
                i.info()
    def showVisitingCards(self):
        for i in self.__database:
            if i.type == "wizytówka":
                i.info()








