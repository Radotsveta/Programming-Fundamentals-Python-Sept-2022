num_of_lines = int(input())

for char in range(num_of_lines):
    number = int(input())
    if not number % 2 == 0:
        print(f'{number} is odd!')
        break
else:
    print('All numbers are even.')