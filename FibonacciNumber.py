def FibonacciNumber(n):
    if n <= 0:
        return "Incorrect"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    fib_0, fib_1 = 0, 1
    for _ in range(3, n+1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1

print(FibonacciNumber(10))