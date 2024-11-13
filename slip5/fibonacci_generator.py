## cd slip5
## python fibonacci_generator.py

## Write a python script to generate Fibonacci terms using generator function

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage:
if __name__ == "__main__":
    # Create a generator object
    fib_gen = fibonacci_generator()
    
    # Generate the first 10 Fibonacci numbers
    for i in range(5):
        print(next(fib_gen))
