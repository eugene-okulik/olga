my_dict = {'tuple': (1, 2, 3, 4, 5),
           'list': ['one', 'two', 7, 95, False],
           'dict': {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
           'set': {3, 4, 5, 6, 7}
           }

print(my_dict['tuple'][-1])
my_dict['list'].append(42)
my_dict['list'].pop(1)
my_dict['dict'][('I am a tuple', )] = (32)
del my_dict['dict']['one']
my_dict['set'].add(42)
my_dict['set'].pop()
print(my_dict)
