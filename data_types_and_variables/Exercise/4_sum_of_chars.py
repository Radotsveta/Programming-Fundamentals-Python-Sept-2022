number_of_char_lines = int(input())
total_sum = 0

for char in range(1, number_of_char_lines + 1):
    letter = input()
    letter_into_ascii = ord(letter)
    total_sum += letter_into_ascii

print(f'The sum equals: {total_sum}')