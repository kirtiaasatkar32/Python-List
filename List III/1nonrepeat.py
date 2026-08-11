"""1. First Non-Repeating Number
   ====================================================================
Scenario
An online voting system stores vote IDs in a list.
Find the first vote ID that appears only once.
Requirements
* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message
Test Case 1
Input:
[4, 5, 1, 2, 1, 2, 4]
Output:
First Non-Repeating Number = 5
Test Case 2
Input:
[7, 7, 8, 8]
Output:
No Non-Repeating Number Found"""
#____________________________________________________________________________________________________

n = int(input("Enter length: "))

a = []

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

found = False

for i in range(n):
    if a.count(a[i]) == 1:
        print("First Non-Repeating Number =", a[i])
        found = True
        break

if found == False:
    print("No Non-Repeating Number Found")