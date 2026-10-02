text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
       'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
text = text.split()
for words in text:
    if words.endswith(','):
        print(words.replace(',', '') + 'ing' + ',')
    elif words.endswith('.'):
        print(words.replace('.', '') + 'ing' + '.')
    elif words:
        print(words + 'ing')
