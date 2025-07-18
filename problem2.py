# The code will print prime numbers 
# The user can get how many they want to print  by giving a simple number
# If he ask 10 prime number then he should give the input as 10. So that first 10 prime numbers will print.


a = int(input("Enter a number: "))
odd_numbers = [2 * i + 1 for i in range(a)]
print(", ".join(map(str, odd_numbers)))
