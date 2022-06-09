vragen = []
vragen.append('Je bent op het strand aan het zwemmen en je zwemt te ver weg. Je spoelt ver weg aan op een eiland en moet nu zien te overleven en het begint nacht te worden. Maak je een [kampvuur] of ga je [slapen]. ')
vragen.append('Het is ochtend. Ga je [zwemmen] of een [hut] bouwen ')
vragen.append('Nu dat je een hut hebt ga je [verkennen] of [aandacht] trekken. ')
vragen.append('Vliegtuigen kunnen nu zien dat je hulp nodig hebt. Je begint honger te krijgen en dus ga je het eiland bekijken. Ga je [oost] of ga je [west]? ')
vragen.append('Je hebt het warm. Ga je [onder] de appelboom genieten van je appel of ga je na het eten de [zee] in. ')
vragen.append('Je pakt wat extra appels en gaat terug naar je hut. Als je thuis aankomt zie je een boot aankomen. [Eet] je op de boot de appels of [niet]. ')

antwoord = []
antwoord.append('kampvuur')
antwoord.append('hut')
antwoord.append('aandacht')
antwoord.append('oost')
antwoord.append('onder')

gameover = ['Je bent dood']


def controleervraag(vraag, antwoord):
    uitkomst = input(vraag).lower()
    if (uitkomst == antwoord):
        return True
    else:
        return False

for x,y in enumerate(vragen):
    if not controleervraag(y, antwoord[x]):
        print('Je bent dood')
        break



