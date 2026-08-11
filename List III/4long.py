"""4. Longest Consecutive Sequence
===============================
Scenario
Find the longest sequence of consecutive numbers present in the list.
Requirements
* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length
Test Case 1
Input:
[100, 4, 200, 1, 3, 2]
Output:
Longest Consecutive Length = 4
Explanation:
Sequence = 1, 2, 3, 4
Test Case 2
Input:
[10, 11, 12, 20]
Output:
Longest Consecutive Length = 3"""
#__________________________________________________________________________

n = int(input("Enter length: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

longest = 0

for i in arr:
    count = 1
    next_num = i + 1

    while next_num in arr:
        count += 1
        next_num += 1

    if count > longest:
        longest = count

print("Longest Consecutive Length =", longest)