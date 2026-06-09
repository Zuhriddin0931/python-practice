# dictionary ichidagi telefonlarni model bo‘yicha tartiblaymiz
def sortlash(ls):
    # model bo‘yicha kamayish tartibida sort
    ls1 = sorted(ls, key=lambda x: x["model"], reverse=True)
    print(ls1)


ls = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

sortlash(ls)