# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 01/28/2025
# Description: ibonacci sequence

def fib(n):
    if n == 1 or n == 2:
        return 1
    
      prev1, prev2 = 1, 1
    
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev1, prev2 = prev2, current
    
    return prev2
