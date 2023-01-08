from abc import ABC
class Card(ABC):
    def __init__(self, type,id):
        self.type = type
        self.id = id
    def __info__(self):
        pass

class Note(Card):
    id = 0
    def __init__(self, title, content):
        super().__init__("notatka", 0)
        self.title = title
        Note.id += 1
        self.id = Note.id
        self.content = content
    def info(self):
        print("ID: ",self.id)
        print("Tytuł: ",self.title)
        print("Treść notatki: ",self.content)

class VisitingCard(Card):
    id = 0
    def __init__(self, firstName, lastName, telephone):
        super().__init__("wizytówka", 0)
        VisitingCard.id += 1
        self.id = VisitingCard.id
        self.firstName = firstName
        self.lastName = lastName
        self.telephone = telephone
    def info(self):
        print("ID: ", self.id)
        print("Imię: ", self.firstName)
        print("Nazwisko: ", self.lastName)
        print("Telefon: ",self.telephone)

