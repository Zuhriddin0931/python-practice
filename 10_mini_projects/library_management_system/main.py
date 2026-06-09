# Kutubxona funksiyalarini import qilamiz
from baza import *

while True:
    tanlov = int(input("""Bo'lajak programmistlar kutubxonasiga xush kelibsiz!!!
    Quyidagi menyudan birini tanlang
        1. Ko'rish
        2. Kiritish
        3. O'chirish
        4. O'zgartirish
        5. Qidirish (Nomi boyicha)
        6. Qatordagi kitoblar
        7. Yili boyicha chiqarish
        8. Janri boyicha chiqarish
        9. Toifasi boyicha chiqarish
        0. Chiqish\n"""
    ))
    # Barcha kitoblarni chiqarish
    if tanlov == 1:
        chiqarish()
    # Yangi kitob qo'shish
    elif tanlov == 2:
        qator = input("Qator raqami: ")
        nomi = input("Kitob nomi: ")
        janri = input("Kitob janri: ")
        toifa = input("Toifa: ")
        yili = input("Yili: ")
        kritish(qator,nomi,janri,toifa,yili)
    # Kitobni o'chirish
    elif tanlov == 3:
        ochirish()
    # Kitob ma'lumotlarini o'zgartirish
    elif tanlov == 4:
        ozgartirish()
    # Kitob nomi bo'yicha qidirish
    elif tanlov == 5:
        nom = input("Kitob nomi: ")
        kitob_nomi_qidir(nom)
    # Qator bo'yicha kitoblarni chiqarish
    elif tanlov == 6:
        qatordagi=int(input("Qaysi qatordagi kitoblar kerak: "))
        qator_boyicha_korsatish(qatordagi)
    # Yil bo'yicha qidirish
    elif tanlov == 7:
        yil=int(input("Kitob yilini kiriting: "))
        yilini_korsatish(yil)
    # Janr bo'yicha qidirish
    elif tanlov == 8:
        janri=input("Janrni kiriting: ")
        janri_qidirish(janri)
    # Toifa bo'yicha qidirish
    elif tanlov == 9:
        toifa=input("Toifani kiriting (Kattalar,bolalar,o'smirlar): ")
        toifa_boyicha(toifa)
    # Dasturdan chiqish
    elif tanlov == 0:
        break