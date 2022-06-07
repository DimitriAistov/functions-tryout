def helloWorld(teller):
    loop = teller
    teller = 1
    while (loop != '0'): 
        print(teller,'Hello world!')
        if (loop == 1): 
            break
        else:
            loop = loop - 1
            teller = teller + 1
            continue 

helloWorld(7)