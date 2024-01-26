def dic(n):
    a = {}

    for i in range(1, n +1):
        a[i] = i * i

    return a

n = int(input("Enter the value of n: "))
square = dic(n)

print("Generated dictionary:")
print(square)
