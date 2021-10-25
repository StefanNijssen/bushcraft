leeftijd = int(input("Wat is uw leeftijd?"))
beschikbaar = int(input("Hoeveel dagen per week bent u beschikbaar?"))
positief = int(input("Op een schaal van 1 tot 10. Hoe positief staat u in het leven"))
doorzetting = int(input("Op een schaal van 1 tot 10. Hoe doorzettend bent u?"))

def standaard():
    geaccepteerd = leeftijd >= 16 and beschikbaar > 3 and positief >= 7 and doorzetting >= 7
    toevoegen = ""
    if geaccepteerd == False:
        print("U bent niet toegelaten")
    elif beer() == True:
        toevoegen += "beer, "
    if bever() == True:
        toevoegen += "bever, "
    if vos() == True:
        toevoegen += "vos, "
    if uil() == True:
        toevoegen += "uil."
    else:
        print("U bent niet toegelaten")
    print("U komt in aanmerking voor " + toevoegen)

def beer():
    sport = int(input("Hoeveel keer per week ga je naar sportschool."))
    lengte = int(input("Hoe lang ben je?"))
    beren = sport >= 4 and lengte >= 190
    return beren

def vos():
    niveau = input("Welk niveau heb je gedaan of doe je? Gym/VWO/HAVO/MAVO/Kader")
    vangen = int(input("Hoe groot schat u de kans dat u een dier kan vangen van 1 tot 10?"))
    vossen = vangen >= 7 and niveau == "Gym" or "VWO" or "HAVO"
    return vossen

def bever():
    bewerking = int(input("Op een schaal van 1 tot 10. Hoe goed bent u met het bewerken van materialen."))
    bouwen = int(input("Op een schaal van 1 tot 10. Hoe goed bent u met het bouwen van hutten enz."))
    bevers = bouwen >= 7 and bewerking >= 7
    return bevers

def uil():
    water = int(input("Op een schaal van 1 tot 10. Hoe goed denkt u water te kunnen zuiveren?"))
    eten = int(input("Op een schaal van 1 tot 10. Hoe goed denkt u eten en drinken te kunnen verzorgen in de natuur?"))
    genezen = int(input("Op een schaal van 1 tot 10. Hoe goed denkt u wonden te kunnen genezen?"))
    verwarmen = int(input("Op een schaal van 1 tot 10. Hoe goed denkt u warmte te kunnen creeëren?"))
    uilen = water >= 7 and eten >= 7 and genezen >= 7 and verwarmen >= 7
    return uilen

standaard()