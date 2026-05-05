# while loop to count from 1-5
# current_number = 1
# while current_number <= 5:
    # print(current_number)
    # current_number += 1

# while loop to count from 1-10 printing only 
# odd numbers and continue

current_number = 0
while current_number < 10:
    current_number += 1
    # if this test passes then the rest of code
    # is ignored and reset back to the start of
    # loop
    if current_number % 2 == 0:
        continue

    print(current_number)

