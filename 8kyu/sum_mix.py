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
import random
computer=['Rock','Scissors','Paper']
computer_results=random.choice(computer)
print(computer_results)
user_choice = input("Enter your choices 'Rock','Scissors','Paper':")
print(user_choice)
if computer_results==user_choice:
    print("draw")

elif (user_choice=='Rock'and computer_results=='Scissors') or\
     (user_choice=='Paper'and computer_results=='Rock') or\
     (user_choice=='Scissors'and computer_results=='Paper'):
    print("user wins")       
else:
    print("computer wins")
    
    