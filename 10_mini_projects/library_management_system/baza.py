kitoblar = [
    # 1-qator (1–10)
    {"qator": 1, "nomi": "Don Quixote", "janri": "Romantika", "toifa": "Kattalar", "yili": 1605},
    {"qator": 1, "nomi": "Pride and Prejudice", "janri": "Roman", "toifa": "Kattalar", "yili": 1813},
    {"qator": 1, "nomi": "Moby-Dick", "janri": "Sarguzasht", "toifa": "Kattalar", "yili": 1851},
    {"qator": 1, "nomi": "War and Peace", "janri": "Tarixiy Roman", "toifa": "Kattalar", "yili": 1869},
    {"qator": 1, "nomi": "Hamlet", "janri": "Tragediya", "toifa": "Kattalar", "yili": 1603},
    {"qator": 1, "nomi": "The Odyssey", "janri": "Epik she’r", "toifa": "Kattalar", "yili": -700},
    {"qator": 1, "nomi": "Crime and Punishment", "janri": "Psixologik Roman", "toifa": "Kattalar", "yili": 1866},
    {"qator": 1, "nomi": "The Great Gatsby", "janri": "Tragediya", "toifa": "Kattalar", "yili": 1925},
    {"qator": 1, "nomi": "The Hobbit", "janri": "Fantastika", "toifa": "Bolalar", "yili": 1937},
    {"qator": 1, "nomi": "One Hundred Years of Solitude", "janri": "Magik realizm", "toifa": "Osmirlar", "yili": 1967},

    # 2-qator (11–20)
    {"qator": 2, "nomi": "Ulysses", "janri": "Modern Roman", "toifa": "Kattalar", "yili": 1922},
    {"qator": 2, "nomi": "Jane Eyre", "janri": "Roman", "toifa": "Kattalar", "yili": 1847},
    {"qator": 2, "nomi": "The Divine Comedy", "janri": "Epik sher", "toifa": "Kattalar", "yili": 1320},
    {"qator": 2, "nomi": "The Catcher in the Rye", "janri": "Roman", "toifa": "Osmirlar", "yili": 1951},
    {"qator": 2, "nomi": "Wuthering Heights", "janri": "Roman", "toifa": "Osmirlar", "yili": 1847},
    {"qator": 2, "nomi": "Anna Karenina", "janri": "Roman", "toifa": "Kattalar", "yili": 1877},
    {"qator": 2, "nomi": "Les Miserables", "janri": "Tarixiy Roman", "toifa": "Kattalar", "yili": 1862},
    {"qator": 2, "nomi": "Fahrenheit 451", "janri": "Fantastika", "toifa": "Osmirlar", "yili": 1953},
    {"qator": 2, "nomi": "Brave New World", "janri": "Fantastika", "toifa": "Bolalar", "yili": 1932},
    {"qator": 2, "nomi": "The Lord of the Rings", "janri": "Fantastika", "toifa": "Osmirlar", "yili": 1954},

    # 3-qator (21–30)
    {"qator": 3, "nomi": "The Iliad", "janri": "Epik sher", "toifa": "Kattalar", "yili": -750},
    {"qator": 3, "nomi": "Don Juan", "janri": "Satira", "toifa": "Kattalar", "yili": 1630},
    {"qator": 3, "nomi": "Dracula", "janri": "G‘oyibiy", "toifa": "Kattalar", "yili": 1897},
    {"qator": 3, "nomi": "Alices Adventures in Wonderland", "janri": "Fantastika", "toifa": "Bolalar", "yili": 1865},
    {"qator": 3, "nomi": "The Great Expectations", "janri": "Roman", "toifa": "Osmirlar", "yili": 1861},
    {"qator": 3, "nomi": "The Scarlet Letter", "janri": "Roman", "toifa": "Osmirlar", "yili": 1850},
    {"qator": 3, "nomi": "Frankenstein", "janri": "G‘oyibiy", "toifa": "Bolalar", "yili": 1818},
    {"qator": 3, "nomi": "Dr Jekyll and Mr Hyde", "janri": "Goyibiy", "toifa": "Osmirlar", "yili": 1886},
    {"qator": 3, "nomi": "Paradise Lost", "janri": "Epik sher", "toifa": "Bolalar", "yili": 1667},
    {"qator": 3, "nomi": "Peter Pan", "janri": "Fantastika", "toifa": "Bolalar", "yili": 1911}
]

fayl = open('kutubxona.txt', 'w', encoding='utf-8')
for i, kitob in enumerate(kitoblar):
    fayl.write(f"{kitob['qator']}\t{kitob['nomi']}\t{kitob['janri']}\t{kitob['toifa']}\t{kitob['yili']}\n")
fayl.close()


def korsatish() -> list:
    ekranga = []

    with open("kutubxona.txt", "r", encoding="utf-8") as fayl:
        data = fayl.read().strip()

    for talaba in data.split("\n"):
        qiymatlar = talaba.split("\t")
        lugat = {
            "qator": int(qiymatlar[0]),
            "nomi": qiymatlar[1],
            "janri": qiymatlar[2],
            "toifa": qiymatlar[3],
            "yili": int(qiymatlar[4])
        }
        ekranga.append(lugat)

    return ekranga

def chiqarish():
    kitoblar1 = korsatish()
    for kitob in kitoblar1:
        print(
            f"|| {kitob['qator']:<5} || {kitob['nomi']:<25} || {kitob['janri']:<15} || {kitob['toifa']:<10} || {kitob['yili']:<5} ||")

def kritish(qator,nomi,janri,toifa,yili):
    with open("kutubxona.txt", "a", encoding="utf-8") as fayl:
        fayl.write(f"{qator}\t{nomi}\t{janri}\t{toifa}\t{yili}\n")

    print("Yangi kitob qo'shildi!")




def ochirish(tanlov):

    with open("kutubxona.txt", "r", encoding="utf-8") as fayl:
        data = fayl.read().strip().split("\n")

    for i, qator in enumerate(data, start=1):
        print(f"{i}. {qator}")


    tanlov = int(input("Ochirmoqchi bolgan kitob raqami yozing: "))


    if 1 <= tanlov <= len(data):
        data.pop(tanlov - 1)
        print("Kitob o'chirildi!")
    else:
        print("Bunday raqam mavjud emas!")

    with open("kutubxona.txt", "w", encoding="utf-8") as fayl:
        for qator in data:
            fayl.write(qator + "\n")


def ozgartirish():
    with open("kutubxona.txt", "r", encoding="utf-8") as fayl:
        data = fayl.read().strip().split("\n")

    for i, qator in enumerate(data, start=1):
        print(f"{i}. {qator}")

    tanlov = int(input("O'zgartirmoqchi bo'lgan kitob raqami: "))

    if 1 <= tanlov <= len(data):

        kitob_qator = data[tanlov - 1].split("\t")

        qator_yangi = input(f"Qator raqami [{kitob_qator[0]}]: ") or kitob_qator[0]
        nomi_yangi = input(f"Kitob nomi [{kitob_qator[1]}]: ") or kitob_qator[1]
        janri_yangi = input(f"Kitob janri [{kitob_qator[2]}]: ") or kitob_qator[2]
        toifa_yangi = input(f"Toifa [{kitob_qator[3]}]: ") or kitob_qator[3]
        yili_yangi = input(f"Yili [{kitob_qator[4]}]: ") or kitob_qator[4]

        data[tanlov - 1] = f"{qator_yangi}\t{nomi_yangi}\t{janri_yangi}\t{toifa_yangi}\t{yili_yangi}"

        with open("kutubxona.txt", "w", encoding="utf-8") as fayl:
            for qator in data:
                fayl.write(qator + "\n")

        print("Kitob muvaffaqiyatli o'zgartirildi!")
    else:
        print("Bunday raqam mavjud emas!")

def kitob_nomi_qidir(nom: str):
    with open("kutubxona.txt","r"):
        kitoblar2=korsatish()
        for kitob in kitoblar2:
            if kitob['nomi'].lower().startswith(nom.lower()):
                print(
                    f"|| {kitob['qator']:<5} || {kitob['nomi']:<25} || {kitob['janri']:<15} || {kitob['toifa']:<10} || {kitob['yili']:<5} ||")


def qator_boyicha_korsatish(qator: int):
    with open("kutubxona.txt","r"):
        kitoblar = korsatish()
        topildi = False
        for kitob in kitoblar:
            if kitob["qator"] == qator:
                print(
                    f"|| {kitob['qator']:<3} || {kitob['nomi']:<30} || "
                    f"{kitob['janri']:<20} || {kitob['toifa']:<10} || {kitob['yili']:<5} ||"
                )
                topildi = True

        if not topildi:
            print("Bu qator bo'yicha kitob topilmadi.")

def yilini_korsatish(yil:int):
    with open("kutubxona.txt","r"):
        kitoblar = korsatish()
        topildi = False
        for kitob in kitoblar:
            if kitob["yili"] == yil:
                print(
                    f"|| {kitob['qator']:<3} || {kitob['nomi']:<30} || "
                    f"{kitob['janri']:<20} || {kitob['toifa']:<10} || {kitob['yili']:<5} ||"
                )
                topildi = True

        if not topildi:
            print("Bu yil bo'yicha kitoblar topilmadi !")

def janri_qidirish(janr:str):
    with open("kutubxona.txt","r"):

        kitoblar2=korsatish()
        for kitob in kitoblar2:
            if kitob['janri'].lower().startswith(janr.lower()):
                print(
                    f"|| {kitob['qator']:<5} || {kitob['nomi']:<25} || {kitob['janri']:<15} || {kitob['toifa']:<10} || {kitob['yili']:<5} ||")
def toifa_boyicha(toifa:str):
    with open("kutubxona.txt","r"):
        kitoblar2=korsatish()
        for kitob in kitoblar2:
            if kitob['toifa'].lower().startswith(toifa.lower()):
                print(
                    f"|| {kitob['qator']:<5} || {kitob['nomi']:<25} || {kitob['janri']:<15} || {kitob['toifa']:<10} || {kitob['yili']:<5} ||")