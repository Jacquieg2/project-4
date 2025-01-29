# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 01/28/2025
# Description: Hailstone
def fall_distance(time):
    """
    Calculate the distance an object falls due to gravity in a given time.

    The formula used is:
        d = (1/2) * g * t^2
    where:
        d = distance in meters,
        g = 9.8 m/s^2 (acceleration due to gravity),
        t = time in seconds.

    Parameters:
    time (float): The time in seconds the object has been falling.

    Returns:
    float: The distance in meters the object has fallen.
    """
    g = 9.8  # Acceleration due to gravity in m/s^2
    distance = 0.5 * g * time ** 2
    return distance
