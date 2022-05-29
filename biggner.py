n=int(input())
n=str(n)
first_number=int(n[0])
second_number=int(n[1])
third_number=int(n[2])
number_of_digits=int(len(n))
sum_of_cubes_of_digits= (first_number ** number_of_digits) + (second_number ** number_of_digits) + (third_number ** number_of_digits)
n=int(n)
if sum_of_cubes_of_digits == n:
    print("True")
else:
    print("False")