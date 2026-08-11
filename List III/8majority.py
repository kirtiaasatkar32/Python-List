"""8. Majority Element Detector
============================
Scenario
Find an element occurring more than N/2 times.
Requirements
* Read N and list elements from user
* Find majority element
* If not present, display appropriate message
Test Case 1
Input:
[2, 2, 1, 2, 3, 2, 2]
Output:
Majority Element = 2
Test Case 2
Input:
[1, 2, 3, 4]
Output:
No Majority Element Found"""
#___________________________________________________________________
n = int(input("Enter length: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

found = False

for i in arr:
    if arr.count(i) > n / 2:
        print("Majority Element =", i)
        found = True
        break

if found == False:
    print("No Majority Element Found")