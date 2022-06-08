n=input()
first_number=int(n[0])
second_number=int(n[1])
one_of_the_digits_is_9=first_number == 9 or second_number == 9
n=int(n)
reminder=n % 9
number_is_multiple_of_9= reminder == 0
if number_is_multiple_of_9 or one_of_the_digits_is_9:
    print("Lucky Number")
else:
    print("Unlucky Number")
