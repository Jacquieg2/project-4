# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 01/28/2025
# Description: Hailstone
def hailstone(n):
    """
    Compute the number of steps required to reach 1 in the hailstone sequence.

    Parameters:
    n (int): A positive integer, the starting number of the sequence.

    Returns:
    int: The number of steps required to reach 1.
    """
    steps = 0

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1

    return steps

