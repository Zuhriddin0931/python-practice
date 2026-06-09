# list ichidan juft sonlarni recursion orqali chiqarish
def juft(x, i=0):
    # base case: list tugasa to‘xtaydi
    if i == len(x):
        return

    # agar juft bo‘lsa chiqaramiz
    if x[i] % 2 == 0:
        print(x[i], end=" ")

    # keyingi elementga o‘tamiz
    juft(x, i + 1)


if __name__ == "__main__":
    lis = [1, 2, 3, 4, 5, 6, 7, 8]
    juft(lis)