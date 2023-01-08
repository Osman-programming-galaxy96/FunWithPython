
import sys
from organiser import Organiser
def main():
    while True:
        button = input('''Wybierz: \r\n
        [1] - dodaj notatkę \r\n
        [2] - dodaj wizytówkę \r\n
        [3] - wyświetl notatki \r\n
        [4] - wyświetl wizytówki \r\n
        [5] - usuń notatkę \r\n
        [6] - usuń wizytówkę \r\n
        [0] - zamknij organizer '''
                       )
        switcher(button)

def switcher(button):
    if(button == "1"):
        note = Organiser()
        note.addNote()
    elif(button == "2"):
        visitCard = Organiser()
        visitCard.addVisitCard()
    elif(button == "3"):
        note = Organiser()
        note.showNotes()
    elif(button =="4"):
        visitCard = Organiser()
        visitCard.showVisitingCards()
    elif(button == "5"):
        note = Organiser()
        note.deleteNote()
    elif(button =="6"):
        visitCard = Organiser()
        visitCard.deleteVisitingCard()
    else:
        sys.exit()

if __name__ == '__main__':
    main()