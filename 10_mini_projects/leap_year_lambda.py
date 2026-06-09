# kabisa yilini tekshiruvchi funksiya
def kabisa(yil):
    return (lambda: yil % 400 == 0 or (yil % 4 == 0 and yil % 100 != 0))


yil = int(input("Yil kiriting: "))

# lambda ni chaqiramiz
natija = kabisa(yil)()

print(natija)