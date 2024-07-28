import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def orientation(p, q, r):
    # Return the orientation of the triplet (p, q, r)
    # 0 -> p, q and r are collinear
    # 1 -> Clockwise
    # 2 -> Counterclockwise
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def graham_scan(points):
    # Find the point with the lowest y-coordinate, break ties by x-coordinate
    min_y_point = min(points, key=lambda p: (p.y, p.x))
    points.pop(points.index(min_y_point))

    # Sort the points based on polar angle with the base point
    points.sort(key=lambda p: (orientation(min_y_point, p, min_y_point), (min_y_point.x - p.x)**2 + (min_y_point.y - p.y)**2))
    
    # Add the base point back to the beginning
    points.insert(0, min_y_point)

    # Create an empty stack and push first three points
    hull = []
    for point in points[:3]:
        hull.append(point)

    # Process the remaining points
    for p in points[3:]:
        while len(hull) > 1 and orientation(hull[-2], hull[-1], p) != 2:
            hull.pop()
        hull.append(p)

    return hull

# Example usage
points = [Point(0, 3), Point(2, 3), Point(1, 1), Point(2, 1), Point(3, 0), Point(0, 0), Point(3, 3),Point(5,2)]
hull = graham_scan(points)

# Print the result
print("Convex Hull:")
for point in hull:
    print(point)

# Optional: Plot the points and the convex hull
def plot_convex_hull(points, hull):
    x_points = [p.x for p in points]
    y_points = [p.y for p in points]
    plt.scatter(x_points, y_points)

    hull.append(hull[0])  # To form a closed loop
    hx = [p.x for p in hull]
    hy = [p.y for p in hull]
    plt.plot(hx, hy, 'r-')

    plt.show()

plot_convex_hull(points, hull)


'''
Point Class: A simple class to represent a point in 2D space.
Orientation Function: Determines the orientation of an ordered triplet (p, q, r).
Graham Scan Function:
Finds the point with the lowest y-coordinate (or leftmost in case of a tie).
Sorts the points based on the polar angle with respect to this base point.
Uses a stack to build the convex hull by iterating through the sorted points and ensuring the hull remains convex.
Example Usage: Defines a set of points and computes the convex hull using the graham_scan function.
Plotting (Optional): Uses matplotlib to visualize the points and the resulting convex hull.
'''

