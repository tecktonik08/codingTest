# import sys
#
# A, B, C = sys.stdin.readline().split()
# A = int(A)
# B = int(B)
# C = int(C)
#
# print((A + B) % C)
# print(((A % C) + (B % C)) % C)
# print((A * B) % C)
# print(((A % C) * (B % C)) % C)

import sys
import math

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))
