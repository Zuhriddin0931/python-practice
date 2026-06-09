# 2 ta set
set1 = {4, 5, 6, 7, 8, 9}
set2 = {5, 6, 7, 10, 11}

# umumiy elementlar
set3 = set1.intersection(set2)

# farqli elementlar
set4 = set1.symmetric_difference(set2)

y = 0
y2 = 0

# intersection yig‘indisi
for son in set3:
    y += son

# symmetric difference yig‘indisi
for son in set4:
    y2 += son

# farqini chiqaramiz
print(y2 - y)