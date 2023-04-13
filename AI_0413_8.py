exam = [];
sum = 0;

for i in range (1, 6):

    x = int(input(f"{i}번째 점수입력:"));
    exam.append(x);

    sum = sum + x;

print("입력된 점수 :", exam);
print("점수의 합 :", sum);
print("점수의 평균 :", sum / 5);
print("최고점수 :", max(exam));
print("최저점수 :", min(exam));
