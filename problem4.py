# It count how many numbers in the list are multiples of each number from 1 to 9 and 
# store it in a dictionary.


numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
result = {i: 0 for i in range(1, 10)}
for n in numbers:
    for i in range(1, 10):
        if n % i == 0:
            result[i] += 1

print(result)
