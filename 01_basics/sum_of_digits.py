# 3 xonali son kiritamiz
print("3 xonali son kiriting")
son = int(input())

# Har bir xonani ajratib olamiz
yuzlik = son // 100
onlik = son // 10 % 10
birlik = son % 10

# Raqamlar yig‘indisini hisoblaymiz
yigindi = yuzlik + onlik + birlik

# Natijani chiqaramiz
print("Raqamlar yigindisi:", yigindi)