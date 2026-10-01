for x in range(1, 100):
    if x % 3 == 0 and x % 5 == 0:
        print('FuzzBuzz')
    elif x % 5 == 0:
        print('Buzz')
    elif x % 3 == 0:
        print('Fuzz')
    else:
        print(x)
