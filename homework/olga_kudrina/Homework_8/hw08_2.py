def fib_gen(limit=200000):
    first_num = 0
    second_num = 1
    summ = first_num + second_num
    count = 1
    while count < limit:
        yield summ
        first_num = second_num
        second_num = summ
        summ = first_num + second_num
        count += 1


count = 1
for element in fib_gen(1000000):
    count += 1
    if count == 5:
        print(element)
    elif count == 200:
        print(element)
    elif count == 1000:
        print(element)
    elif count == 100000:
        print(element)
        break
