words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

# Добавила два варианта решения, с функцией и без нее

# for word in words:
#     print(word * int(words[word]))


def multiply_values(k, v):
    return k * v


for word in words:
    print(multiply_values(word, words[word]))
