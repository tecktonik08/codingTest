n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(a)
print(b)
# 이코테 답
a.sort()
b.sort(reverse=True)
print(a)
print(b)
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

# 내가 해본 풀이
# for n in range(k): # n이 활용되지 않음
#
#     for i in range(len(a)-1):
#         if a[i] < a[i+1]: # 이 부분 min으로 수정
#             min = a[i]
#         else:
#             min = a[i+1]
#
#     for j in range(len(b)-1):
#         if b[j] > b[j+1]: # 이 부분 max로 수정
#             max = b[j]
#         else:
#             max = b[j+1]
#
#
#     a[a.index(min)], b[b.index(max)] = b[b.index(max)], a[a.index(min)]

# for n in range(k):
#     for i in range(len(a)):
#         if a[i] == min(a):
#             for j in range(len(b)):
#                 if b[j] == max(b):
#                     a[i], b[j] = b[j], a[i]

# for n in range(k):
#     for i in range(len(a)):
#         if a[i] == min(a):
#     for j in range(len(b)):
#         if b[j] == max(b):
#             a[i], b[j] = b[j], a[i]
#
# for i, j in zip(a, b):  # k번 반복 x
#     print(min(a), max(b))
print(a,b)
print(sum(a))
