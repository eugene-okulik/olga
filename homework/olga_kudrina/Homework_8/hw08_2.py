import sys
sys.set_int_max_str_digits(1000000)


def fib_gen():
    first_num = 0
    second_num = 1
    summ = first_num + second_num
    count = 1
    while True:
        yield summ
        first_num = second_num
        second_num = summ
        summ = first_num + second_num
        count += 1


count = 1
for element in fib_gen():
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
