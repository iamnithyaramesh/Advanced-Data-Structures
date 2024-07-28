def quickhull(points):
    if len(points) <= 1:
        return points

    def get_extreme_points(points):
        min_point = max_point = points[0]
        for p in points[1:]:
            if p[0] < min_point[0]:
                min_point = p
            if p[0] > max_point[0]:
                max_point = p
        return min_point, max_point

    def distance(point, line_start, line_end):
        return abs((line_end[1] - line_start[1]) * point[0] - (line_end[0] - line_start[0]) * point[1] + line_end[0] * line_start[1] - line_end[1] * line_start[0]) / ((line_end[1] - line_start[1])**2 + (line_end[0] - line_start[0])**2)**0.5

    def is_left_of_line(point, line_start, line_end):
        return (line_end[0] - line_start[0]) * (point[1] - line_start[1]) - (line_end[1] - line_start[1]) * (point[0] - line_start[0]) > 0

    def find_hull(points, line_start, line_end):
        if not points:
            return []

        farthest_point = max(points, key=lambda p: distance(p, line_start, line_end))
        points.remove(farthest_point)

        left_set = [p for p in points if is_left_of_line(p, line_start, farthest_point)]
        right_set = [p for p in points if is_left_of_line(p, farthest_point, line_end)]

        return find_hull(left_set, line_start, farthest_point) + [farthest_point] + find_hull(right_set, farthest_point, line_end)

    min_point, max_point = get_extreme_points(points)
    left_set = [p for p in points if is_left_of_line(p, min_point, max_point)]
    right_set = [p for p in points if is_left_of_line(p, max_point, min_point)]

    return [min_point] + find_hull(left_set, min_point, max_point) + [max_point] + find_hull(right_set, max_point, min_point)

# Example usage
points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
hull = quickhull(points)
print("Convex Hull:", hull)
