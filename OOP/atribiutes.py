from abc import ABC
class Card(ABC):
    def __init__(self, type):
        self.type = type
    def __info__(self):
        pass

class Note(Card):
    def __init__(self, title, content):
        super().__init__("notatka")
        self.title = title
        self.content = content
    def info(self):
        print(self.title)
        print(self.content)

class VisitingCard(Card):
    def __init__(self, firstName, lastName, telephone):
        super().__init__("wizytówka")
        self.firstName = firstName
        self.lastName = lastName
        self.telephone = telephone
    def info(self):
        print("Imię: ", self.firstName)
        print("Nazwisko: ", self.lastName)
        print("Telefon: ",self.telephone)

