#The program asks the user for input N (positive integer) and reads it
N = int(input("Enter a positive integer N: "))
while N <= 0:
    N = int(input("Please enter a positive integer N: "))

#Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)

numbers = []
for i in range(N):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
#asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputed it before.
X = int(input("Enter an integer X: "))
found = False
for i in range(N):
    if numbers[i] == X:
        print(f"Index of {X} is {i + 1}")
        found = True
        break
if not found:
    print("-1")