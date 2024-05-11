# Python program to generate Fibonacci sequence up to n terms

def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Generate Fibonacci sequence up to 10 terms
fib_sequence = fibonacci(10)
print("Fibonacci sequence:", fib_sequence)
