import math

group_size = int(input())
days = int(input())
total_money = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    if day % 3 == 0:
        total_money -= 3 * group_size
    if day % 5 == 0:
        total_money += 20 * group_size
        if day % 3 == 0:
            total_money -= 2 * group_size
    total_money += 50
    total_money -= 2 * group_size

coins_per_companion = math.floor(total_money / group_size)
print(f'{group_size} companions received {coins_per_companion} coins each.')