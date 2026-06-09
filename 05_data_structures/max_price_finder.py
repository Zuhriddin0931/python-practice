# mahsulotlar narxlari
prices = {"Olma": 10000, "Nok": 15000, "Banan": 20000}

dic = {}

# eng katta qiymatni topamiz
m = max(prices.values())

# shu qiymatga teng bo‘lganlarni olamiz
for k, v in prices.items():
    if v == m:
        dic[k] = v

print(dic)