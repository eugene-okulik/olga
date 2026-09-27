person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

a = 'результат операции: 42'
start = a.index(':') + 2
result = int(a[start:]) + 10
print("a:", result)

b = 'результат операции: 514'
start = b.index(':') + 2
result = int(b[start:]) + 10
print('b:', result)

c = 'результат работы программы: 9'
start = c.index(':') + 2
result = int(c[start:]) + 10
print('c:', result)

# Добавила еще два варианта решения

# d = 'результат операции: 42'
# start = d.index(':')
# result = int((d[start:]).lstrip(': '))
# print('d:', result + 10)

# e = 'результат операции: 42'
# splitnum = int(e.split(':')[1])
# print('e:', splitnum + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
