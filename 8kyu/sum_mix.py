#Given an array of integers as strings and numbers, 
# return the sum of the array values as if all were numbers.

#Return your answer as a number.
#my_solution
# def sum_mix(arr):
#     return sum(int(x) for x in arr)

# arr = ['1',2,'3']

# print(sum_mix(arr))
# print(26 & 23)
# a=8
# print(id(a))
# a=9
# print(id(a))
# print(a is a)
#the given number prime or not
# number = int(input("Enter a number:"))
# if number%2==0:
#     print("its a even number")
# else:
#     print("its a odd number")

# year =int(input("Enter the year:"))
# if year%4==0:
#     if year%100!=0 or year%400==0:
#         print("its a leap year")
#     else:
#         print('its not a leap year')
# else:
#     print("its not a leap year")
# import random
# names =input("Enter the names:")
# mylist=names.split(",")



# print(mylist)
# selected =random.choices(mylist)
# print(selected)
# my_list =[[4,5,6],[1,2,3],[7,8,9]]
# choice1 = int(input("Enter the row:"))
# choice2 = int(input("Enter the column:"))
# print(my_list)
# my_list[choice1][choice2]="*"
# for row in my_list:
#     print(row)
# import random
# computer=['Rock','Scissors','Paper']
# computer_results=random.choice(computer)
# print(computer_results)
# user_choice = input("Enter your choices 'Rock','Scissors','Paper':")
# print(user_choice)
# if computer_results==user_choice:
#     print("draw")

# elif (user_choice=='Rock'and computer_results=='Scissors') or\
#      (user_choice=='Paper'and computer_results=='Rock') or\
#      (user_choice=='Scissors'and computer_results=='Paper'):
#     print("user wins")       
# else:
#     print("computer wins")
#program to calculate average height from the list
# l1=[60,40]
# total =0
# my_list = len(l1)
# for i in l1:
#     total+=i
# average = total//my_list
# print(average)
# myList= input("enter the numers of list:")
# actual_list=myList.split(",")
# list1 =[]
# list1.append(myList)
# print(list1)

# total =0
# for i in actual_list:
#     total+=int(i)
# my_length = len(actual_list)
# print(my_length)
# print(total)
# my_list_heights =input("Enter the list:")
# actual_list = my_list_heights.split(",")
# count =0
# for height in actual_list:
#     count+=1
# print(count)
# total=0
# for i in range(len(actual_list)):
#     actual_list[i]= int(actual_list[i])
#     total+=i
#     print(count)
#     average =total/count
# print(round(average))
# heights =input("enter the heights of the list:")
# my_list = heights.split(",")
# count =0
# for height in my_list:
#     count+=1
# print(count)
# for i in range(count):
#     my_list[i]=int(my_list[i])

# print(my_list)

# total =0
# for i in my_list:
#     total+=i
# print(total)
# print(count)
# avg = total/count
# print(round(avg))
# Find maximum number from the given List
# my_list = input("Enter the numbers:")
# actual = my_list.split(",")
# count =0
# for n in actual:
#     count+=1
# for i in range(count):
#      actual[i]=int(actual[i])
# max_value=actual[0]
# for i in actual:
#     if i>max_value:
#         max_value=i
# print(max_value)
# total=0
# for i in range(1,101):
#     total+=i
# print(total)
#calculate sum of even numbers from 1 to 100 including 1 and 100
# sum=0
# for i in range(1,101):
#     if i%2==0:
#         sum+=i
# print(sum)
        
#Fizz Buzz
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("fizzbuzz")
#     elif i%5==0:
#          print("buzz")
#     elif i%3==0:
#          print("fizz")
#     else:
#         print(i)
# Prime number or not
# def prime_number(n1):
#     if n1<=1:
#         return False
#     for i in range(2,int(n1+1)):
#         if n1%i==0:
#             return False
#     return True
        
# print(prime_number(3))
# student_marks = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 88,
#     "Esha": 95
# }

# def get_grade(mark):
#     if 90<=mark<=100:
#         return "A+"
#     elif 81<=mark<=89:
#         return "A"
#     elif 71<=mark<=80:
#         return "B+"
#     elif 61<=mark<=70:
#         return "B"
#     elif 51<=mark<=60:
#         return "C"
#     elif 51<=mark<=40:
#         return "B"
#     else:
#         return "F"
    
    
    
# for name,mark in student_marks.items():
#     grade = get_grade(mark)
#     print(f"{name}:{mark}->{grade}")
# student_data=[{"Name":"Ram","roll_no":10,"age":20,"course":"Python"}]
# def add_student_datat(name,rollno,age,course):
#     student={
#         "name":name,
#         "rollno":rollno,
#         "age":age,
#         "course":course
#     }
    
#     student_data.append(student)
#     return student_data
    
# print(add_student_datat("sumi",1121,37,'python'))
# my_dictionary ={}

# def myinfo(name,price):
#     my_dictionary[name]=price
# while True:
#     name =input("Enter your name:")
#     price=int(input("Enter your bidding amount:"))
#     myinfo(name,price)
#     another = input("do u want to add another bidder yes/no").lower()
#     if another!='yes':
#         break
    

# print(my_dictionary)
# max_bidder = max(my_dictionary,key=my_dictionary.get)
# print(max_bidder)

def leap_year(year):
    return  (year%4==0 and year%100!=0) or (year%400==0)
def my_findings(year,month):
    leap=leap_year(year)
    find_month={
        "january": 31,
        "february": 29 if leap_year else 28,
        "march": 31,
        "april": 30,
        "may": 31,
        "june": 30,
        "july": 31,
        "august": 31,
        "september": 30,
        "october": 31,
        "november": 30,
        "december": 31
    }
    return find_month.get(month,"invalid")


year = int(input("enter the year:"))
month = input("Enter the month:").lower()
result = my_findings(year,month)
print(result)



