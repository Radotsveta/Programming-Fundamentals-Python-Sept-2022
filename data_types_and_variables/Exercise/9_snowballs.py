# number_of_snowballs = int(input())
# highest_snowball_value = 0
# highest_snowball_weight = 0
# highest_snowball_time = 0
# highest_snowball_quality = 0
#
# for snowball in range(number_of_snowballs):
#     snowball_weight = int(input())
#     needed_time = int(input())
#     quality = int(input())
#     snowball_value = (snowball_weight / needed_time) ** quality
#     if snowball_value > highest_snowball_value:
#         highest_snowball_value = snowball_value
#         highest_snowball_weight = snowball_weight
#         highest_snowball_time = needed_time
#         highest_snowball_quality = quality
#
# print(f'{highest_snowball_weight} : {highest_snowball_time} '
#       f'= {int(highest_snowball_value)} ({highest_snowball_quality})')



lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmets_count = lost_fights_count // 2
broken_swords_count = lost_fights_count // 3
broken_shields_count = lost_fights_count // 6
broken_armors_count = broken_shields_count // 2

helmet_expenses = broken_helmets_count * helmet_price
sword_expenses = broken_swords_count * sword_price
shield_expenses = broken_shields_count * shield_price
armor_expenses = broken_armors_count * armor_price
total_expenses = helmet_expenses + sword_expenses + shield_expenses + armor_price

print(f'Gladiator expenses: {total_expenses:.2f} aureus')