import random as r;

for i in range(0, 30):

    number = r.randint(1, 51);
    
    if (number % 3 == 0 and number % 5 == 0):

        print("발생한 난수는? " + str(number) + ": 3 과 5의 배수 fizzbuzz")

    elif(number % 3 == 0):

        print("발생한 난수는? " + str(number) + ": 3의 배수 fizz")

    elif(number % 5 == 0):

        print("발생한 난수는? " + str(number) + ": 5의 배수 buzz")