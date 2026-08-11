"""7. Array Rotation Analyzer
==========================
Scenario
Rotate the array K times towards the right.
Requirements
* Read N and list elements from user
* Read K
* Rotate the array
* Display rotated array
Test Case 1
Input:
Array = [1, 2, 3, 4, 5]
K = 2
Output:
[4, 5, 1, 2, 3]
Test Case 2
Input:
Array = [10, 20, 30, 40]
K = 1
Output:
[40, 10, 20, 30]"""
#_________________________________________________

arr = []

n = int(input("Enter length: "))

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

k = int(input("Enter K: "))

for i in range(k):
    last = arr.pop()
    arr.insert(0, last)

print(arr)