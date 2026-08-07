"""
Question 3: Industrial Sensor Peak Energy Monitoring System

Problem:
    Find all peak energy values and perform the required analysis.

Tasks:
    - Find all peak values
    - Compute sum of squares
    - Compute average
    - Find difference between maximum and minimum peak

Input:
    A list of integers.

Output:
    Peaks, Sum of Squares, Average, Difference

Test Cases:
    Input : [20, 40, 30, 60, 50]
    Output:
        Peaks = [40, 60]
        Sum of Squares = 5200
        Average = 50
        Difference = 20

    Input : [10, 20, 15, 25, 20, 30]
    Output:
        Peaks = [20, 25, 30]
        Sum of Squares = 1525
        Average = 25
        Difference = 10

    Input : [5]
    Output:
        Peaks = [5]
        Sum of Squares = 25
        Average = 5
        Difference = 0
"""
arr=list(map(int,input("Enter Energy value : ").split(" ")))
n=len(arr)
peak=[]
for i in range(n):
    if i==0:
        if n==1 or arr[i] >= arr[i+1]:
            peak.append(arr[i])
    elif i==n-1:
        if arr[i]>=arr[i-1]:
            peak.append(arr[i])
    else:
        if arr[i] >= arr[i-1] and arr[i]>= arr[i+1]:
            peak.append(arr[i])
sum_square=0
for i in peak:
    sum_square=sum_square+(i*i)

avg=sum(peak)//len(peak)
diff=max(peak)-min(peak)

print("Peaks =", peak)
print("Sum of Squares =", sum_square)
print("Average =", avg)
print("Difference =", diff)










































