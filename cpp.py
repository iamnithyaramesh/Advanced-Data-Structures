import math

def brute_force(points, n):

    if n == 2:
        return math.sqrt((points[0][0]-points[1][0])**2 + (points[0][1] - points[1][1])**2)

    if n == 3:
        min_dist = float('inf')
        for i in range(3):
            for j in range(3):
                d =  math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1] - points[j][1])**2)
                if d < min_dist and d != 0:
                    min_dist = d
        return min_dist


def sort_by_x(points):
    sorted_points = sorted(points, key=lambda coord: coord[0])
    return sorted_points

def sort_by_y(points):
    sorted_points = sorted(points, key=lambda coord: coord[1])
    return sorted_points

def find_min_in_strip(points, size , d):
    points = sort_by_y(points)
    if size > 7:
        size = 7
    min_dist = d
    for i in range(size):
        for j in range(i+1, size):
                if points[j][1] - points[i][1] >= min_dist:
                    break
                d = math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1] - points[j][1])**2)
                if d < min_dist and d != 0:
                    min_points = [points[i], points[j]]
                    min_dist = d
    return min_dist

def find_min(points, n):

    points = sort_by_x(points)

    if n <= 3:
        return brute_force(points, n)

    mid = n // 2
    midPoint = points[mid]
    left = find_min(points[:mid], mid)
    right = find_min(points[mid:], n - mid)
    min_dist = min(left, right)

    strip = []
    for i in range(n):
        if abs(points[i][0] - midPoint[0]) < min_dist:
            strip.append(points[i])
    return find_min_in_strip(strip, len(strip), min_dist)

import random
points = [(random.randint(1,100), random.randint(1,100)) for _ in range(20)]

import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
plt.switch_backend('Qt5Agg')
import random

points = [(random.randint(1,100), random.randint(1,100)) for _ in range(20)]

n = len(points)
print("Minimum distance:", find_min(points, n))
print(points)
x = [point[0] for point in points]
y = [point[1] for point in points]

plt.scatter(x, y)
plt.show()


    
    

    