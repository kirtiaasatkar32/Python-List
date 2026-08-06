"""1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3"""
#________________________________________________________________________________________

n=int(input("Enter Marks: "))
marks=[]
count=0
for i in range(n):
    x=int(input("Enter marks: "))
    if x > 75:
        count+=1
    marks.append(x)
print(marks)
print("Highest = ",max(marks))
print("Lowest = ",min(marks))
print("count above 75 = ",count)