n=int(input())
if n%3 == 0 and n%2 ==0:
    print("Number is divisible by 6")
if (n%3 == 0 and not(n%2 == 0)):
    print("Number is divisible by 3")
if (not(n%3 == 0) and n%2==0):
    print("Number is divisible by 2")
if (not(n%3 == 0) and not(n%2 == 0)):
    print("Number is not divisible by 2, 3 or 6")