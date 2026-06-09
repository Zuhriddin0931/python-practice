# 2 ta listni solishtirib umumiy elementlarni topamiz
def kesish(ls, ls1):
    # lambda orqali tekshiruvchi funksiya
    tekshir = lambda x: x in ls1

    natija = []

    # har bir elementni tekshiramiz
    for x in ls:
        if tekshir(x):
            natija.append(x)

    print(natija)


ls = [1, 2, 3, 5, 7, 8, 9, 10]
ls1 = [1, 2, 4, 8, 9]

kesish(ls, ls1)