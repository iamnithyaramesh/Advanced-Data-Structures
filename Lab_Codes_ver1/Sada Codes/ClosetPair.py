import math

def distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def brute_force(points):
    """Find the smallest distance between points using brute force."""
    min_dist = float('inf')
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
    return min_dist

def find_min_in_strip(strip, d):
    """Find the smallest distance in a vertical strip."""
    strip.sort(key=lambda coord: coord[1])  # Sort strip according to y coordinate
    min_dist = d
    size = len(strip)
    for i in range(size):
        for j in range(i + 1, size):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break
            d = distance(strip[i], strip[j])
            if d < min_dist:
                min_dist = d
    return min_dist

def find_min(points):
    """Recursively find the smallest distance between points."""
    points.sort(key=lambda coord: coord[0])  # Sort points according to x coordinate
    n = len(points)

    if n <= 3:
        return brute_force(points)

    mid = n // 2
    midPoint = points[mid]

    left_min = find_min(points[:mid])
    right_min = find_min(points[mid:])

    min_dist = min(left_min, right_min)

    # Create a strip that contains points close to the midpoint
    strip = [point for point in points if abs(point[0] - midPoint[0]) < min_dist]

    return min(find_min_in_strip(strip, min_dist), min_dist)
