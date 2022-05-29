# Bignner-python-programin
#indexing
w=input()
n=input()
n=int(n)
print(w[n])

# Last character of the string
word=input()
n = len(word)
print(word[n-1])

# Half string 
word=input()
n= len(word)
half_string=int(n/2)
print(word[0:half_string])

#string Repetition
word=input()
n=input()
n=int(n)
print(word * n)

#string Repetition method
word=input()
n=input()
print(word[len(word)-3: ] * int(n))

#sum of digits of a number
n=input()
print(int(n[0]) + int(n[1]) + int(n[2]))

# bignner-python-day2

#Area of Triangle
length=input()
length=int(length)
breadth=input()
breadth=int(breadth)
area_of_rectangle= length * breadth
print(area_of_rectangle)

#Perimeter of Triangle
length=input()
length=int(length)
breadth=input()
breadth=int(breadth)
perimeter=2 *(length+breadth)
print(perimeter)

#Kilometers to meters convertion
kilometer=input()
kilometer=float(kilometer)
meters=int(kilometer * 1000)
print(meters)

#Length of given string input
w=input()
w=len(w)
print(w)

#String Slicing
w=input()
w=w[:3]
print(w)

#Comparing first three characters of given two string inputs using slicing and printing boolean o/p
w=input()
x=input()
y=w[:3]
z=x[:3]
print(y == z)

#Comparing given two inputs
w=input()
w=int(w)
x=input()
x=int(x)
y=(w>0 and x>0)
z=(w>5 or x>5)
print(y and z)

#Comparing digits of a given number
w=input()
x=(int(w)>25)
y=int(w[0])
z=int(w[1])
a=(y>z)
print(x and a)

#Reverse of given input strings
w=input()
x=input()
reverse_of_x=x
reverse_of_w=w
print(reverse_of_x)
print("---")
print(reverse_of_w)

#Comparing last three characters of a string
w=input()
x=input()
lengthw=len(w)
lengthx=len(x)
last_three_of_w=w[(lengthw-3):]
last_three_of_x=x[lengthx-3:]
print(last_three_of_w == last_three_of_x)

#Printing first letters of the given inputs
w=input()
x=input()
y=input()
first_character_of_w=w[0]
first_character_of_x=x[0]
first_character_of_y=y[0]
print(first_character_of_w + first_character_of_x + first_character_of_y)

#printing half string 
string=input()
length=len(string)
half_string_len=length//2
print(string[half_string_len:])

#String repetetion
w=input()
n=input()
n=int(n)     
print((w+" ")*n )  #We can only concatinate strings

#Printing first and last digits of a number
n=input()
m=len(n)
first_digtit=n[0]
last_dight=n[m-1]
print(first_digtit)
print(last_dight)

#Checking whether given numbers is present inbtween range
a=input()
a=int(a)
b=input()
b=int(b)
c=input()
c=int(c)
print((10<=a<=20) or (10<=b<=20) or (10<=c<=20))

#Printing women population when men_population=52% and total_population is given input
total_population=int(input())
men_population=52
total_men_population=total_population * (men_population/100)
total_women_population=total_population - total_men_population
print(int(total_women_population))

#Converting given integer input to years,weeks and days
n= input()
n= int(n)
one_year= 365
number_of_years= int(n/one_year)
print(number_of_years)
number_of_weeks= int((n-(number_of_years*one_year))/7)
print(number_of_weeks)
number_of_days=(n-((number_of_years*one_year)+(number_of_weeks*7)))
print(number_of_days)

#skipping Letter
word=input()
n=int(input())
print(word[:n]+word[n+1:])



