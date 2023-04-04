# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

even_numbers = []

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)

# 2. Print the difference between the largest and smallest value:

print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.

for i in range(len(numbers)):
    if numbers[i] == 2 and (numbers[i] == numbers[i+1] or numbers[i] == numbers[i-1]):
        print(True)
        break

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

counter = 0
sum_of_numbers = 0

while counter < len(numbers):
    if numbers[counter] == 6:
        while numbers[counter] != 7:
            counter += 1
    else:
        sum_of_numbers += numbers[counter]
    #sum_of_numbers = numbers[counter]
    counter += 1

print(sum_of_numbers)



# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

counter = 0
sum_of_numbers_2 = 0

# while counter < len(numbers):
#     if numbers[counter] == 13:
#             counter += 1
#     else:
#         sum_of_numbers_2 += numbers[counter]
#     #sum_of_numbers = numbers[counter]
#     counter += 1

# print(sum_of_numbers_2)

for i in range(len(numbers)):
    if numbers[i] == 13 or numbers[i-1] == 13:
        continue
    else:
        sum_of_numbers_2 += numbers[i]
print(sum_of_numbers_2)







