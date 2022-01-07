import math
m = 4
n = 3
puddles = [[2, 2]]
# 전체 경로 수(wh) - 물웅덩이 지나는 경로 수(sp)
# 전체 경로 수 구하기
wh = int(math.factorial((m-1) + (n-1)) / math.factorial(m-1) / math.factorial(n-1))
# sp 경로 수 구하기 (sp1 : 시작점~물웅덩이, sp2 : 물웅덩이 ~ 도착점)
x = puddles[0][0]
y = puddles[0][1]
sp1 = int(math.factorial((x-1)+(y-1)) / math.factorial(x-1) * math.factorial(y-1))
sp2 = int(math.factorial((m-1)-(x-1)+(n-1)-(y-1)) / math.factorial((m-1)-(x-1)) * math.factorial((n-1)-(y-1)))
sp = sp1 * sp2
answer = wh - sp
print(answer)