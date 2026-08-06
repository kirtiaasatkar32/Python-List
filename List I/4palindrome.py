"""4.Palindrome Number List Checker
Scenario
A system checks lucky numbers which are palindromes.
Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases
Input:
[121, 131, 20, 44, 55, 100]
Output:
Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]"""
#_____________________________________________________________________

n=int(input("Enter Number of Elements =  "))
numbers=[]
palindrome=[]
for i in range(n):
    x=int(input("Enter Number = "))
    numbers.append(x)
print("List = ",numbers)
largest=0
for num in numbers:
    temp=num
    rev=0
    while temp>0:
        digit = temp%10
        rev=rev*10+digit
        temp=temp//10
    if num==rev:
        palindrome.append(num)
        if num>largest:
            largest=num
print("Palindromes = ",palindrome)
print("Count = ",len(palindrome))

if len(palindrome)==0:
    print("Largest = Not Available")
else:
    print("Largest = ",largest)
palindrome.sort()
print("Sorted = ",palindrome)












   