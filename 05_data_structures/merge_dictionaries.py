# 2 ta dictionary
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

dic = {}

# 1-dictionary ni ko‘chiramiz
for key, value in d1.items():
    dic[key] = value

# 2-dictionary ni qo‘shamiz (agar key bo‘lsa, yig‘amiz)
for k, v in d2.items():
    if k in dic:
        dic[k] = dic[k] + v
    else:
        dic[k] = v

print(dic)