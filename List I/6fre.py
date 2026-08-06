"""6. Frequency Count of Elements (Advanced Scenario-Based Problem)
A government survey department collects responses from different regions. Each response is stored as an integer in a list (representing selected option IDs).
The department wants to analyze:
* How many times each option was selected
* Most popular option
* Least popular option
* Detect invalid entries (negative numbers or zeros)
 Requirements
Write a Python program to:
1. Store survey responses in a list
2. Ignore invalid entries (≤ 0)
3. Count frequency of each valid number
4. Display frequency in sorted order
5. Find the most frequently selected option
6. Find the least frequently selected option (excluding invalid data)
7. Store frequency in a dictionary
NOTE:
* Avoid using built-in `Counter`
## Input Format
A list of integers representing responses.
# Scenario 1: Normal Survey Data
## Input
[1, 2, 2, 3, 3, 3, 4, 1, 2]
## Output
Frequency Count:
1 → 2
2 → 3
3 → 3
4 → 1
Most Frequent: 2 or 3 (tie)
Least Frequent: 4
# Scenario 2: Data with Invalid Entries
## Input
[1, 2, -1, 3, 0, 2, 4, -5, 3, 3]
## Output
Invalid Entries Ignored: [-1, 0, -5]
Frequency Count:
1 → 1
2 → 2
3 → 3
4 → 1
Most Frequent: 3
Least Frequent: 1 or 4
# Scenario 3: Highly Skewed Data
## Input
[5, 5, 5, 5, 2, 2, 1]
## Output
Frequency Count:
1 → 1
2 → 2
5 → 4
Most Frequent: 5
Least Frequent: 1
# Scenario 4: All Same Values
## Input
[7, 7, 7, 7, 7]
## Output
Frequency Count:
7 → 5
Most Frequent: 7
Least Frequent: 7
# Scenario 5: Empty / Invalid Only Data
## Input
[-1, 0, -3]
## Output
No valid data found"""
#________________________________________________________________________________________
n=int(input("Enter size : "))
enteries=[]
valid=[]
invalid=[]

for i in range(1,n+1):
    a=int(input(f"The Survey {i} : "))
    if a<0:
        invalid.append(a)
    else:
        valid.append(a)
print("Valid List : ",valid)
print("Invalid List : ",invalid)

if len(valid)==0:
    print("No valid Data Found")
else:
    valid.sort()
    visit=[]
    max=[]
    least=[]
    maxcount=0
    mincount=len(valid)
    
    print("Frequency Count ")
    for i in valid:
        found=False
        for j in visit:
            if i==j:
                found=True
                break
        if found:
            continue
        count=0
        for j in valid:
            if j==i:
                count+=1
        print(f"{i} -----> {count}")
        visit.append(i)
    if count > maxcount:
        maxcount=count
        max=[i]
    elif count == maxcount:
        max.append(i)
    if count<mincount:
        mincount=count
        least=[i]
    elif count==mincount:
        least.append(i)
    if len(invalid)>0:
        print("\nInvalid Enterprise Ignored : ",invalid)
    print("\nMost Frequent : ",max)
    print("Least Frequent : ",least)


