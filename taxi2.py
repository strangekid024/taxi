fees = []
tmp= input().split()
N = int(tmp[0])
X = int(tmp[1])
for _ in range(N):
    tmpn = input().split()
    hatsu_kyori = int(tmpn[0])
    hatsu_un = int(tmpn[1])
    kasan_kyori = int(tmpn[2])
    kasan_un = int(tmpn[3])
    if X <  hatsu_kyori:
        result = hatsu_un
        fees.append(result)
    elif X >= hatsu_kyori:
        portion = (X-hatsu_kyori)/kasan_kyori
        result = hatsu_un + int(portion +1)*kasan_un
        fees.append(result)
print(min(fees),max(fees))