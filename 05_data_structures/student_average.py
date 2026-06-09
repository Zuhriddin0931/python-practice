# o‘quvchilar va baholar
dic = {
  "Ali": {"math": 80, "eng": 90, "prog": 85},
  "Vali": {"math": 70, "eng": 75, "prog": 80}
}

d = {}

# har bir student uchun o‘rtacha hisoblaymiz
for k, v in dic.items():
    s = sum(v.values())
    uzunligi = len(v)
    orta = s / uzunligi
    d[k] = orta

print(d)