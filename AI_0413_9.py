import random as r;

solution = r.randint(10, 100);

user = int(input("복권번호(10-99)를 입력하시오 : "));

digit_1 = int(solution / 10);
digit_2 = int(solution % 10);

u_digit_1 = int(user / 10);
u_digit_2  = int(user % 10);

print(f"당첨 번호는 {solution}입니다.");

if (digit_1 == u_digit_1 and digit_2 == u_digit_2):

    print("상금은 100만원입니다.");

elif (digit_1 == u_digit_1 or digit_2 == u_digit_2 or digit_1 == u_digit_2 or digit_2 == u_digit_1):

    print("상금은 50만원입니다.");

else:

    print("상금은 없습니다.");