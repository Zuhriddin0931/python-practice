# 3 ta kompaniya setlari
set1 = {"Artel", "Alif", "Yandex", "Google", "Meta"}
set2 = {"Google", "Apple", "Amazon", "Meta"}
set3 = {"Alibaba", "Uzum", "Meta", "Google", "Amazon"}

# set2 va set3 ning umumiylari
set4 = set2.intersection(set3)

# set1 dan set4 dagilarni ayiramiz
natija = set1.difference(set4)

print(natija)