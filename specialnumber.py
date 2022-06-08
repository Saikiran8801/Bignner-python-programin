n=input()
first_digit=int(n[0])
second_digit=int(n[1])
sum_of_digits=((first_digit)+(second_digit) == 7)
one_of_thedigits=first_digit == 7 or second_digit == 7
n=int(n)
reminder= n % 7
is_multiple_of_7=reminder == 0
if sum_of_digits or one_of_thedigits or is_multiple_of_7:
    print("Special Number")
else:
    print("Normal Number")
