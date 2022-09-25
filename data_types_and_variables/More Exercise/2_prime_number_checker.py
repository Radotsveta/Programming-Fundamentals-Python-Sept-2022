number = int(input())
is_number_prime = True

for not_prime_num in range(2, number):
    if number % not_prime_num == 0:
        is_number_prime = False
        break
print(is_number_prime)