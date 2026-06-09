# Foydalanuvchidan fayl hajmini kiritamiz (MB yoki GB)
print("Fayl hajmini kiriting")
fayl_hajmi = float(input())

# Internet tezligini kiritamiz (MB/s)
print("Tezligini kiriting")
tezlik = float(input())

# Yuklab olish vaqtini hisoblaymiz
vaqt = (fayl_hajmi * 8) / tezlik

# Natijani chiqaramiz
print("Fayl", vaqt, "soniyada yuklanadi")