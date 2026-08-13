"""3.MATRIX PERFORMANCE EVALUATION SYSTEM
A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.
The HR department wants a menu-driven application to analyze employee performance.
Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45"""
#___________________________________________________________________________________________
r, c = map(int, input("Enter Rows and Columns: ").split())

arr = []

for i in range(r):
    row = list(map(int, input("Enter elements: ").split()))
    arr.append(row)

while True:

    print("\n1. Find Employee with Highest Total Score")
    print("2. Find Month with Lowest Average Score")
    print("3. Display Employee-wise Maximum Score")
    print("4. Exit")

    choice = input("Enter choice: ")

    match choice:

        case "1":
            total = []

            for row in arr:
                total.append(sum(row))

            highest = max(total)
            employee = total.index(highest) + 1

            print("Employee", employee, "has Highest Total Score =", highest)

        case "2":
            average = []

            for j in range(c):
                total = 0

                for i in range(r):
                    total = total + arr[i][j]

                average.append(total / r)

            lowest = min(average)
            month = average.index(lowest) + 1

            print("Month", month, "Average =", lowest)

        case "3":
            for i in range(r):
                print("Employee", i + 1, "Max Score =", max(arr[i]))

        case "4":
            print("Thank You")
            break

        case _:
            print("Invalid Choice")