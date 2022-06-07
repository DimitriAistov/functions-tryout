def fibonacci():
    a,b = 0,1
    for A in range(20):
        print(str(A+1) + ': ' + str(a))
        a,b = b,a+b
        print('ratio: ' + str(a/b))
fibonacci()