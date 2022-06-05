length_a=int(input())
length_b=int(input())
length_c=int(input())
if((((length_a+length_b)>length_c) and ((length_b+length_c)>length_a)) and ((length_c+length_a)>length_b)):
    print("It's a Triangle")
else:
    print("It's not a Triangle")