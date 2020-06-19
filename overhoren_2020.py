import os
import sys
import random
import time

def strepen():
    print("="*40)


def welkom_keuze():
    strepen()
    print("Welkom bij overhoor progamma van Issam!")
    print("Tip: begin met een woordenlijst maken!")
    strepen()
    print("Nieuwe lijst: 'n'")
    print("Bekijk lijst: 'b'")
    print("Wijzig lijst: 'w'")
    print("Woord verwijderen: 'x'")
    print("Overhoor lijst: 'o'")
    print("Stop mijn programma: 'q'")
    strepen()

def main():
    welkom_keuze()
    keuze = input("Welke letter geef je mij mee?: ")
    woorden = {}
    while keuze != 'q':
        if (keuze == 'n'):
            woorden = nieuwe_lijst(woorden)
        if (keuze == 'b'):
            bekijk_lijst(woorden)
        if (keuze == 'w'):
            wijzig_lijst(woorden)
        if (keuze == 'x'):
            verwijder_woord(woorden)
        if (keuze == 'o'):
            overhoren_lijst(woorden)
        strepen()
        keuze = input("Welke letter geef je mij mee?: ")
    stoppen()

def nieuwe_lijst(woorden):
    strepen()
    print("'q' om te stoppen")
    print("Laten we beginnen!")
    woorden = {}
    key = input("NE: ")
    if len(key) > 1:
        while key != "q":
            value = input("EN: ")
            woorden[key] = value
            key = input("NE: ")
        f = open('lijstwoorden.txt', 'w')
        for key in woorden:
            f.write("{}:{} ".format(key, woorden[key]))
        f.close()
        print("Je woorden zijn nu toegevoegd!")
        print("Als je nog meer woorden wilt toevoegen, typ dan 'n'.")
        return woorden
    else:
        print("Ik vraag het maar 1 keer vriendelijk, GEBRUIK EEN WOORD GEEN LETTER!")

def bekijk_lijst(woorden):
    strepen()
    print("NL | EN")
    for key in woorden:
        print("{key} : {value}".format(key=key, value=woorden[key]))

def wijzig_lijst(woorden):
    bekijk_lijst(woorden)
    strepen()
    key = input("Woord (NL) dat je wilt veranderen: ")
    newNL = input("Nieuw woord (NL): ")
    newEN = input("Nieuwe vertaling (EN): ")
    woorden[newNL] = newEN
    del woorden[key]
    print("De nieuwe wijziging is aangebracht in je woorden lijst!")
    return woorden

def verwijder_woord(woorden):
    bekijk_lijst(woorden)
    strepen()
    key = input("Welk (NL) woord wil je verwijderen: ")
    vraagdelete = input("Deze actie kan niet ongedaan gemaakt worden. Weet je het zeker? (Y/N) ")
    if (vraagdelete == 'Y'):
        del woorden[key]
    elif (vraagdelete == 'N'):
        return woorden
    else:
        print("Je gaf geen geldige antwood!")

def overhoren_lijst(woorden):
    punten = 0
    while punten < len(woorden.keys())*3:
        strepen()
        NLwoord = random.choice(list(woorden))
        print("Wat is de vertaling van dit woord?")
        ENwoord = input(NLwoord + ": ")
        if (ENwoord == woorden[NLwoord]):
            print("Dat is juist!")
            punten += 1
            print("Aantal punten: ", punten)
        elif (ENwoord == 'q'):
            break
        else:
            print("Dat is helaas fout.")
            print("Het juiste antwoord was:",woorden[NLwoord])
            punten -= 1
    print("Je hebt alle woorden gehad. Aantal punten: ",punten,"/",len(woorden.keys())*3, "punten")

def stoppen():
    print("Dit programma sluit over 5 seconden,")
    print("5")
    time.sleep(0.5)
    print("4")
    time.sleep(0.5)
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("0")
    time.sleep(0.5)
    sys.exit()

main()