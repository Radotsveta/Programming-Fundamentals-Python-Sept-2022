key = int(input())
number_of_lines = int(input())
decrypted_message = ''

for character in range(number_of_lines):
    letter = input()
    letter_in_digit = ord(letter)
    decrypted_letter = letter_in_digit + key
    decrypted_message += chr(decrypted_letter)
print(decrypted_message)