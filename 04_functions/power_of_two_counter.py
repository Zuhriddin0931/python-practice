# sonni 2 ga necha marta bo‘lish mumkinligini hisoblaymiz
def daraja(son, k):
    count = 0

    # son 1 bo‘lmaguncha 2 ga bo‘lamiz
    while son != 1:
        son //= 2
        count += 1

    return count


if __name__ == "__main__":
    son = int(input("Son kiriting: "))
    k = int(input("Qaysi sonning darajasi: "))

    print(daraja(son, k))