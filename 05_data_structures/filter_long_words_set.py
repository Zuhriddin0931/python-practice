# So'zlar to‘plami
words = {"apple", "banana", "cherry", "kiwi"}

# Set ustida loop qilish uchun listga aylantiramiz
w = list(words)

# 5 harfdan uzun so‘zlarni olib tashlaymiz
for soz in w:
    if len(soz) > 5:
        words.discard(soz)

# Natijani chiqaramiz
print(words)