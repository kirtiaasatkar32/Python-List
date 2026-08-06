"""2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []"""
#_________________________________________________________________________________________________
n=int(input("Enter Number of Employee Salary  = "))
salary=[]
for i in range(n):
    x=int(input("Enter Salaries = "))
    salary.append(x)
total_sum=sum(salary)
avg=total_sum//n
print("Average = ",avg)
for i in salary:
    if i > avg:
        print("Above Average = ",i)
for i in salary[:]:
    if i < 15000:
        salary.remove(i)
print("Remaining list = ",salary)
