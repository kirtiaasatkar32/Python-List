"""6. Product Except Self
======================
Scenario
For every element, calculate the product of all other elements except itself.
Requirements
* Read N and list elements from user
* Create a new list containing products
* Display the result
Test Case 1
Input:
[1, 2, 3, 4]
Output:
[24, 12, 8, 6]
Test Case 2
Input:
[2, 3, 5]
Output:
[15, 10, 6]"""
#___________________________________________________________________________________
n = int(input("Enter length: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

result = []

for i in range(n):
    product = 1

    for j in range(n):
        if i != j:
            product = product * arr[j]

    result.append(product)

print(result)