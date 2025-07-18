# It is a program similar to problem2 which prints prime numbers But according to the problem statement and examples
#  ===>if user gives input (n) is EVEN it prints input (n-1) prime numbers. 
#  ===>if user enters ODD number as input (n) then it prints (n) prime numbers. 


a = int(input("Enter a number: "))
if a % 2 == 0:
    a -= 1
odd_numbers = [2 * i + 1 for i in range(a)]
print(", ".join(map(str, odd_numbers)))
