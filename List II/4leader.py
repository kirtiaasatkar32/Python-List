"""4.Problem: Sum of Leaders in an Array After Filtering Invalid Data (Python)
Definition
A company collects daily performance scores of employees. However, the dataset may contain invalid entries.
An element is called a leader if:
It is greater than all elements to its right side
The element must be valid, i.e., it should not be:
Negative number
Zero
Rightmost valid element is always considered a leader.
Input Format
First line → integer n
Second line → n space-separated integers
Output Format
Single integer → sum of all valid leader elements
If no valid elements exist → return -1
Rules
Before finding leaders:
Ignore all negative values and zeros
Work only on positive numbers
Then find leaders from the filtered sequence
Test Case 1
Input:
8
16 0 17 4 -3 3 5 2
Processing:
Filtered array:
[16, 17, 4, 3, 5, 2]
Leaders:
[17, 5, 2]
Output:
24
Test Case 2
Input:
6
-1 0 -5 0 -2 -3
Output:
-1
Test Case 3
Input:
5
10 20 30 40 50
Processing:
Filtered array:
[10, 20, 30, 40, 50]
Leaders:
[50]
Output:
50"""
#___________________________________________________________
n=int(input("Enter Size = "))
arr=list(map(int,input("Enter Numbers = ").split()))
valid=[]
for i in arr:
    if i > 0:
        valid.append(i)
if len(valid)==0:
    print(-1)
else:
    leader=[]
    max=0
    for i in range(len(valid)-1,-1,-1):
        if valid[i]>max:
            leader.append(valid[i])
            max=valid[i]
    leader.reverse()
    print("Filtered Array =", valid)
    print("Leaders =", leader)
    print("Sum =", sum(leader))


























