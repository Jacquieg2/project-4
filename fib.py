# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 01/28/2025
# Description: ibonacci sequence
def fib(n):
    # Handle the first two positions in the Fibonacci sequence
    if n == 1 or n == 2:
        return 1

    # Variables to store the two previous Fibonacci numbers
    prev1, prev2 = 1, 1

    # Iterate from the 3rd term to the nth term
    for _ in range(3, n + 1):
        # Calculate the next Fibonacci number
        current = prev1 + prev2
        # Update the previous two numbers
        prev1, prev2 = prev2, current

    # Return the nth Fibonacci number
    return prev2

