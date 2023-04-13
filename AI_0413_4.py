import random as r;

array = [];
sum = 0;

for i in range (0, 10):

    array.append(r.randint(10, 100));
    sum = sum + array[i];

print(f"리스트 : {array}");
print(f"정수들의 합 : {sum}");