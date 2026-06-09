# Foydalanuvchidan son kiritamiz
son = int(input("Son kiriting: "))

# Son qaysi i^2 va j^2 orasida ekanini topamiz
for i in range(1, son):
    for j in range(2, son + 1):
        if i * i <= son <= j * j:
            son1 = i

# Natijani chiqaramiz
print(son1)