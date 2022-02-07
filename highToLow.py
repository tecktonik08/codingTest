n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

# 책 풀이
# array = sorted(array, reverse=True)
#
# for i in array:
#     print(i, end = ' ')

# 선택 정렬
# for i in range(len(array)):
#     max_index = i                       # 가장 앞쪽 원소
#     for j in range(i+1, len(array)):    # 다음 인덱스부터 반복, 선형탐색
#         if array[max_index] < array[j]:
#             max_index = j               # 가장 큰 원소를 min_index에 담기
#         array[i], array[max_index] = array[max_index], array[i]   # 자리 바꾸기

# 삽입 정렬
# for i in range(1, len(array)):
#     for j in range(i, 0, -1):          # 인덱스 i부터 1까지 감소하여 반복하는 문법
#         if array[j] > array[j - 1]:    # 앞의 숫자보다 크다면
#             array[j], array[j - 1] = array[j - 1], array[j] # 자리 바꿈
#         else:      # 앞의 숫자보다 작다면
#             break  # 멈추고 다음 차례로

# 계수 정렬
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')
