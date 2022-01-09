#nach Eingabe des Geburtstags, wird die bisherige Lebenszeit in 
#Sekunden, Stunden und Tagen ausgegeben

from datetime import datetime

gebUser = input("Wann hast du Geburtstag? (dd.mm.yyyy): ")
try:
    #Aufspalten der Eingabe
    gebUsersplit = gebUser.split(".")
    gebUserTag = int(gebUsersplit[0])
    gebUserMonat = int(gebUsersplit[1])
    gebUserJahr = int(gebUsersplit[2])
    #Syntax von datetime(Jahr, Monat, Tag)
    gebUserDate = datetime(gebUserJahr, gebUserMonat, gebUserTag)

    #Aktuelle Zeit erhalten
    heute = datetime.today()

    alter = heute - gebUserDate
    alterTage = alter.days
    alterStunden = alter.days * 24
    alterMinuten = alterStunden * 60
    alterSekunden = alterMinuten * 60

    print("Dein Alter beträgt: ")
    print(f"{alterTage} Tage")
    print(f"{alterStunden} Stunden")
    print(f"{alterMinuten} Minuten")
    print(f"{alterSekunden} Sekunden")
except ValueError:
    print("Bitte ein richtiges Datum eintragen")