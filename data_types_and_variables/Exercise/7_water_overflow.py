number_of_lines = int(input())
capacity = 255
total_poured_water = 0

for water_pouring in range(number_of_lines):
    current_water_pouring = int(input())
    if capacity - current_water_pouring < 0:
        print(f'Insufficient capacity!')
        continue
    capacity -= current_water_pouring
    total_poured_water += current_water_pouring

print(total_poured_water)