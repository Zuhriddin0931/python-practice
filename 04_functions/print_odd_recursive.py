# 1 dan n gacha bo‘lgan toq sonlarni recursion orqali chiqarish
def toq(n):
    # bazaviy holat: 0 ga yetganda to‘xtaydi
    if n == 0:
        return

    # avval oldingi sonlarni chaqiramiz
    toq(n - 1)

    # agar toq bo‘lsa chiqaramiz
    if n % 2 == 1:
        print(n)


if __name__ == "__main__":
    son = int(input("Son kiriting: "))
    toq(son)