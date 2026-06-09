# 2 ta so‘zni solishtiramiz (katta-kichik harf farqsiz)
def solishtir(soz, soz1):
    # harflarni kichik qilib sort qilamiz
    natija1 = sorted(soz, key=lambda x: x.lower())
    natija2 = sorted(soz1, key=lambda x: x.lower())

    # tengligini tekshiramiz
    return natija1 == natija2


soz = input("Soz kiriting: ")
soz1 = input("Soz kiriting: ")

print(solishtir(soz, soz1))