salary=int(input())
years_of_service=int(input())
if years_of_service>5:
    Bonus=(5/100)*salary
    print(float(Bonus))
else:
    print("No Bonus")