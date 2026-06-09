# Foydalanuvchidan son kiritamiz
son = int(input("Son kiriting: "))

# 1 dan son gacha aylantiramiz
for i in range(1, son + 1):

    # 3 va 5 ga bo‘linsa FizzBuzz
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    # faqat 5 ga bo‘linsa Buzz
    elif i % 5 == 0:
        print("Buzz")

    # faqat 3 ga bo‘linsa Fizz
    elif i % 3 == 0:
        print("Fizz")

    # aks holda sonni chiqaramiz
    else:
        print(i)