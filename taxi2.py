＃コーディング：utf-8
def get_high_and_low(X,hatsu_kyori,hatsu_un,kasan_kyori,kasan_un):
    fees = []
    if X <  hatsu_kyori:
        result = hatsu_un
        fees.append(result)
    elif X >= hatsu_kyori:
        portion = (X-hatsu_kyori)/kasan_kyori
        result = hatsu_un + int(portion +1)*kasan_un
        fees.append(result)
    return(min(fees),max(fees))

n = input('how many')


for _ in range(int(n)):
    X = input('how long')
    hk = input('first_distance')
    hu = input('first_fee')
    kk = input('add_distance')
    ku = input('add_fee')
    r = get_high_and_low(int(X),int(hk),int(hu),int(kk),int(ku))
print(r)
