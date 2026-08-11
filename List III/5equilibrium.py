"""5. Equilibrium Index Finder
===========================
Scenario
Find an index where:
# Sum of elements on the left side
Sum of elements on the right side
Requirements
* Read N and list elements from user
* Find equilibrium index
* If not found, display message
Test Case 1
Input:
[1, 3, 5, 2, 2]
Output:
Equilibrium Index = 2
Explanation:
1 + 3 = 2 + 2
Test Case 2
Input:
[1, 2, 3]
Output:
No Equilibrium Index Found"""
#__________________________________________________________________
arr=list(map(int,input("Enter The Elements : ").split(' ')))
print(arr)

n=len(arr)



for i in range(n):
    Lsum=0
    Rsum=0

    for j in range(0,i):
        Lsum+=arr[j]
    
    for j in range(n-1,i,-1):
        Rsum+=arr[j]

    if Lsum==Rsum:
        print(f"Equilibriumm Index at {i}")
    
        break
else:
    print("not found")