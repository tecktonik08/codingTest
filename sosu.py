M = 3
N = 16
sosu = []
for i in range(M,N+1):
    yak = []
    for j in range(2,i):
        if i % j == 0:
            yak.append(j)
    if len(yak) == 0:
        sosu.append(i)
print(sosu)