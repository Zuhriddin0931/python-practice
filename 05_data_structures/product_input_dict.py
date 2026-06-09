# Bo‘sh dictionary
dic = {}

# Nechta mahsulot kiritilishini so‘raymiz
n = int(input("Nechta mahsulot kiritasiz: "))

# Har bir mahsulotni qo‘shamiz
for i in range(n):
    a = input("Mahsulot nomi: ")
    b = int(input(f"{a} narxi: "))
    dic[a] = b

print(dic)