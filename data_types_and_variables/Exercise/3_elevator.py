# #first_method
#
# number_of_people = int(input())
# capacity = int(input())
#
# full_courses_number = number_of_people // capacity
# if not number_of_people % capacity == 0:
#     full_courses_number += 1
#
# print(full_courses_number)
#
#
# #second_method
#
# number_of_people = int(input())
# capacity = int(input())
#
# full_courses_number = int(number_of_people / capacity)
# if not number_of_people % capacity == 0:
#     full_courses_number += 1
#
# print(full_courses_number)
#

#third_method
import math

number_of_people = int(input())
capacity = int(input())

full_courses_number = math.floor(number_of_people / capacity)
if not number_of_people % capacity == 0:
    full_courses_number += 1

print(full_courses_number)