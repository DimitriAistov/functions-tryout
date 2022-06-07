def naamEnLeeftijd():
    while True:
        naam = input('Naam: ')
        if naam == 'stop':
            break
        leeftijd = input ('Leeftijd: ')
        if leeftijd == 'stop':
            break
        print('Hallo', naam, ' je leeftijd is', leeftijd, '')

naamEnLeeftijd()