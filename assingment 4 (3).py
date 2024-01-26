n = int(input("Enter the value of n: "))
number = []

for i in range(n):
    num = float(input("Enter number ! " + str(i + 1) + " == "))
    number.append(num)

total = sum(number)
print("the list u entered !=!",number)
print("Sum of the", n, "numbers is:", total)
