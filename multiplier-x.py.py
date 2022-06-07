invoerGetal = int(input('Van welk getal 1 t/m 10 wilt u de tafel zien? '))
def tafel(nummer: int):
    for hoeveelheid in range(1,11):
        print(hoeveelheid, 'x', nummer, '=', hoeveelheid * nummer)
tafel(invoerGetal)