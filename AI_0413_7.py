for i in range(2, 21):

    isPrime = True;

    for j in range(2, i - 1):

        if ( i % j == 0 ):

            isPrime = False;

    if (isPrime):

        print(i, end=" ");