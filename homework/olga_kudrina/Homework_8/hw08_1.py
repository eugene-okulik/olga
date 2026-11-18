import random

salary = int(input())
bonus = random.choice([True, False])
bonus_amount = random.randint(1, 100)

if bonus is True:
    total_payout = (salary + bonus_amount)
else:
    total_payout = salary
print(f"{salary} {bonus} - $'{total_payout}'")
