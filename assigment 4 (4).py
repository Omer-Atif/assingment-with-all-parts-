print(''' ?? what is fibronic series ??
      ANSWER ;                                   
    a type series where each number is the sum of the two that precede it. ''') #sir iski defination ma ne googel se nikali ha 
def fibonacci_series(n):
    fib = [0, 1]

    while len(fib) < n:
        next_num = fib[-1] + fib[-2]
        fib.append(next_num)

    return fib

n_value = int(input("Enter the number of terms in the Fibonacci series: "))
result = fibonacci_series(n_value)

print("Fibonacci series with", n_value, "terms:")
print(result)
