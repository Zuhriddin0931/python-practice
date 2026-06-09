# Foydalanuvchidan son kiritamiz
son = input("Son kiriting: ")

# Sonni teskarisiga aylantiramiz
son1 = son[::-1]

# Tekshiramiz: agar teng bo‘lsa palindrom
if son1 == son:
    print("Son palindrom")
else:
    print("Son palindrom emas")