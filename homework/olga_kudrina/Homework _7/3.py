def numb_summ(a, b=10):
    a = int(a.split(':')[-1])
    return a + b


list_strings = ['результат операции: 42', 'результат операции: 54',
                'результат работы программы: 209', 'результат: 2']

for string in list_strings:
    string = numb_summ(string)

    print(string)
