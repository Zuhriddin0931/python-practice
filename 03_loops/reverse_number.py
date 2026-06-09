# Foydalanuvchidan son olamiz
son = int(input("Son kiriting: "))

# Belgini saqlab qolamiz (manfiy yoki musbat)
belgi = 1
if son < 0:
    belgi = -1
    son *= -1

# Teskari sonni yig‘amiz
teskari = 0

# Sonni teskari qilish
while son != 0:
    teskari = teskari * 10 + son % 10
    son //= 10

# Natijani chiqaramiz
print(teskari * belgi)