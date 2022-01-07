import sys

a, b = map(int, sys.stdin.readline().split(' '))

# 최대 공약수 구하기
a_yak = []  # a의 약수
for i in range(1, a + 1):
    if a % i == 0:
        a_yak.append(i)

b_yak = []  # b의 약수
for j in range(1, b + 1):
    if b % j == 0:
        b_yak.append(j)

ab_yak = []  # a,b의 공약수
for i in range(len(a_yak)):
    for j in range(len(b_yak)):
        if a_yak[i] == b_yak[j]:
            ab_yak.append(a_yak[i])

a_mok = a / ab_yak[-1]  # a를 공약수로 나눈수
b_mok = b / ab_yak[-1]  # b를 공약수로 나눈수
ab_bae = ab_yak[-1] * a_mok * b_mok  # ab 최소공배수 = 최대공약수 * 최대공약수로 나눈 a,b의 몫

print(ab_yak[-1])
print(ab_bae)
