import os
import sys
import random
import time

def strepen():
    print("="*40)


def welkom_keuze():
    strepen()
    print("Welkom bij mijn overhoor progamma!")
    print("Tip: begin met een woordenlijst maken!")
    strepen()
    print("Maak Engelse lijst: e; Maak Franse lijst: f; Maak Duitse lijst: d ")
    print("Bekijk Engelse lijst: be; Bekijk Franse lijst: bf; Bekijk Duitse lijst: bd")
    print("Wijzig lijst: w")
    print("Overhoor lijst: o")
    print("Lijst verwijderen: x")
    print("Stop mijn programma: q")
    strepen()

def main():
    welkom_keuze()
    keuze = input("Welke letter geef je mij mee?:")
    woorden = {}
    while keuze != 'q':
        if (keuze == 'b'):
            bekijk_lijst(woorden)
        if (keuze == 'b2'):
            bekijk_lijst2(woorden2)
        if (keuze == 'n'):
            woorden = nieuwe_lijst(woorden)
        if (keuze == 'w'):
            wijzig_lijst(woorden)
        if (keuze == 'e'):
            alletaal(woorden2)
        if (keuze == 'o'):
            overhoren_lijst(woorden)
        if (keuze == 'x'):
            lijst_verwijderen(woorden)
        strepen()
        keuze = input("Welke letter geef je mij mee?: ")
    stoppen()


def bekijk_lijst(woorden):
    strepen()
   # welke_lijst = input("Van welke lijst wil je de woorden zien? (Type 'standaard' voor de engelse versie)(zonder.txt): ")
   # (welke_lijst == 'standaard'):
    print("Nederlands : Engels")
    for key in woorden:
        print("{key} : {value}".format(key=key, value=woorden[key]))
   #else:
     #welke_lijst = welke_lijst + ".txt"
    # bestaat_lijst_overhoor = os.path.isfile(welke_lijst)
     #if bestaat_lijst_overhoor:
      # with open(welke_lijst, "r") as f:
       #print("Nederlands : " + welke_lijst)
        #for key in woorden:
        #   print("{key} : {value}".format(key=key, value=woorden[key]))
        #else:
          #  print("Bestand bestaat niet.")

def bekijk_lijst2(woorden2):
    strepen()
    print("Nederlands : Vertaling")
    for key in woorden2:
      print("{key} : {value}".format(key=key, value=woorden2[key]))


def alletaal(woorden2):
    strepen()
    print ("'q' om te stoppen")
    print("Laten we beginnen!")
    woorden2 = {}
    taal2 = input("Naar welke taal wil je vertalen? ")
    if len(taal2) > 3:
        print("Je hebt gekozen voor taal: " + taal2)
        naambestand = input("Hoe moet je bestand heten? (zonder .txt)")
        with open(naambestand+".txt", "w+") as f:
            f.write("zet er iets in!")
        print("Bestand " + naambestand + ".txt is gemaakt.")
        strepen()
        print("'q' om te stoppenn")
        print("Laten we beginnen!")
        woorden2 = {}
        key = input ("Nederlands: ")
        if len(key) > 1:
            while key != "q":
                value = input(taal2 + ":")
                woorden2[key] = value
                key = input("Nederlands:")
            f = open(naambestand + '.txt', 'w')
            for key in woorden2:
                f.write("{}:{} ".format(key, woorden2[key]))
            f.close
            print("Je bent klaar met je lijst!")
            print("Als je nog meer woorden wilt wijzigen, kan dat in het menu")
            return woorden2
    else:
        print("Schrijf je echte taal, niet cheaten!")

def nieuwe_lijst(woorden):
    strepen()
    print("'q' om te stoppenn")
    print("Laten we beginnen!")
    woorden = {}
    key = input("Nederlands:")
    if len(key) > 1:
        while key != "q":
            value = input("Engels:")
            woorden[key] = value
            key = input("Nederlands:")
        f = open('engels.txt', 'w')
        for key in woorden:
            f.write("{}:{} ".format(key, woorden[key]))
        f.close()
        print("Je bent klaar met je lijst!")
        print("Als je nog meer woorden wilt wijzigen, kan dat in het menu")
        return woorden
    else:
        print("Ik vraag het maar 1 keer vriendelijk, GEBRUIK EEN WOORD GEEN LETTER!")

def wijzig_lijst(woorden):
    bekijk_lijst(woorden)
    strepen()
    key = input("Woord (NL) dat je wilt veranderen:")
    newnl = input("Nieuw woord (NL):")
    newen = input("Nieuwe vertaling(EN):")
    woorden[newnl] = newen
    del woorden[key]
    print("De nieuwe wijziging is aangebracht in je woorden lijst!")
    return woorden

def verwijder_woord(woorden):
    bekijk_lijst(woorden)
    strepen()
    key = input("Woord (NL) die je wilt verwijderen:")
    vraag = input("Weet je zeker dat je dit woord wilt verwijderen?(ja/nee)")
    if (vraag == 'ja'):
        del woorden[key]
    return woorden

def overhoren_lijst(woorden):
    strepen()
    standaard = input("Wil je de standaard lijst of niet (typ 'ja' of 'nee'). ")
    if (standaard == 'ja'):
        punten = 0
        while punten < len(woorden.keys())*2:
            strepen()
            nlwoord = random.choice(list(woorden))
            print("Wat is de vertaling van dit woord?")
            enwoord = input(nlwoord + ":")
            if (enwoord == woorden[nlwoord]):
                print("Dat is juist!")
                punten += 1
                print("Aantal punten: ",punten)
            elif (enwoord == 'q'):
                break
            else:
                print("Dat is helaas fout")
                print("Het goede antwoord:", woorden[nlwoord])
                punten -= 1
                print("Aantal punten: ", punten)
    elif (standaard == 'nee'):
        bestandnaam_overhoor = input("Hoe heet het bestand (zonder .txt)? ")
        bestandnaam_overhoor = bestandnaam_overhoor + ".txt"
        bestaat_bestandnaam = os.path.isfile(bestandnaam_overhoor)
        if bestaat_bestandnaam:
            with open(bestandnaam_overhoor) as f:
                punten  = 0
                while punten < len(woorden.keys())*2:
                    strepen()
                    nl2woord = random.choice(list(woorden2))
                    print("Wat is de vertaling van dit woord?")
                    tawoord = input(nl2woord + ":")
                    if (tawoord == woorden2[nl2woord]):
                        print("Dat is juist!")
                        punten += 1
                        print("Aantal punten: ", punten)
                    elif (tawoord == "q"):
                        break
                    else:
                        print("Dat is helaas fout")
                        print("Het goede antwoord:", woorden2[nl2woord])
                        punten -= 1
                        print("Aantal punten: ", punten)
        else:
            print("Bestand bestaat niet!")

def lijst_verwijderen(woorden):
    strepen()
    del_lijst = input("Welke lijst wil je verwijderen? (zonder .txt) ")
    del_lijst = del_lijst + ".txt"
    bestaat_lijst_del = os.path.isfile(del_lijst)
    if del_lijst == ('engels.txt'):
        print("Dat gaan we niet doen jongetje!")
    elif bestaat_lijst_del:
        os.remove(del_lijst)
        print("Lijst " + del_lijst + " is succesvol verwijdert.")
    else:
        print("Bestand bestaat niet, dus kan het ook niet verwijdert worden!")


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