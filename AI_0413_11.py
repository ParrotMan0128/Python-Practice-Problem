x, y, z = eval(input("3개의 정수를 입력하시오 : "))

if (x > y):

    if (y > z):

        smallest = z;
    
    else:

        smallest = y;

else:

    if (x > z):

        smallest = z;

    else:

        smallest = x;

print(f"제일 작은 정수는 {smallest}입니다s.");