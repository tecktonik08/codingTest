
# N = 10
# answer = 0
# for i in range(1,N+1):  # 1~N 숫자
#     if i == 1:
#         answer = 1
#     else :
#         answer = i * (i-1)
# print(answer)

# 방법 1 : factorial 함수
import math

N = 10
print(math.factorial(N))

# 방법2 : numpy.prod 함수
import numpy as np

N = 10
N_list = [] # empty list
answer = 0  # return 값

for i in range(1, N+1):     # 1~N 수
    N_list.append(i)        # N_list 삽입
answer = np.prod(N_list)    # list 내 모든 값을 곱
print(answer)

# for j in range(1, len(N_list)):
#     if j == len(N_list):
#         break;
#     else:
#         answer = N_list[j] * N_list[j+1]
# print(answer)
#

