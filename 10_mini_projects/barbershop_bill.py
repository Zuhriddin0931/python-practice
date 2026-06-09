# Soch va soqol xizmatlari narxi
soch_narxi = 25000
soqol_narxi = 10000

# Umumiy to'lovni 0 dan boshlaymiz
jami = 0

# Soch olish bo'yicha savol
print("Soch olasizmi?\n1.Ha\n0.Yo'q")
soch = int(input())

# Agar foydalanuvchi ha desa, narx qo‘shiladi
if soch == 1:
    jami += soch_narxi

# Soqol olish bo'yicha savol
print("Soqol olasizmi?\n1.Ha\n0.Yo'q")
soqol = int(input())

# Agar ha bo‘lsa, narx qo‘shiladi
if soqol == 1:
    jami += soqol_narxi

# Umumiy to‘lovni chiqaramiz
print("Jami to‘lov:", jami, "so‘m")