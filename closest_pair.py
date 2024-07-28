class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __repr__(self):
        return f'({self.x}, {self.y})'

def brute_force_closest_pair(lst, n=0):
    distances = []
    n = len(lst)
    for i in lst:
        for j in lst:
            if i.x != j.x or i.y != j.y: 
                d = i.dist(j)
                distances.append(((i, j), d))
    distances.sort(key=lambda pair: pair[1])
    try:
        return distances[0]
    except IndexError: 
        return None

def closest_in_strip(strip, d):
    min_dist = d
    strip = sorted(strip, key=lambda point: point.y)
    for i in range(len(strip)):
        for j in range(i+1, min(i+7, len(strip))): 
            if strip[j].y - strip[i].y >= min_dist:
                break
            if strip[i].dist(strip[j]) < min_dist: 
                min_dist = strip[i].dist(strip[j])
    if min_dist == d:
        return None
    return min_dist

def divide_and_conquer_closest_pair(lst):
    if len(lst) < 3:
        result = brute_force_closest_pair(lst, len(lst))
        if result is not None:
            return result
        else:
            return ((Point(), Point()), float('inf'))
    else:
        x_sorted = sorted(lst, key=lambda p: p.x)
        n = len(lst)
        mid = n // 2
        midPoint = x_sorted[mid]
        dlp = divide_and_conquer_closest_pair(x_sorted[:mid])
        drp = divide_and_conquer_closest_pair(x_sorted[mid:])
        d = min(dlp[1], drp[1])
        strip = [point for point in x_sorted if abs(point.x - midPoint.x) < d]
        mins = [dlp, drp, closest_in_strip(strip, d)]
        mins = [m for m in mins if m is not None]
        if not mins:
            return ((Point(), Point()), float('inf'))
        mins.sort(key=lambda p: p[1])
        return mins[0]

if __name__ == '__main__':
    pl = [Point(0, 3), Point(1, 2), Point(1, 1), Point(5, 7), Point(2, 4), Point(2, 9), Point(1, 4)]
    print(divide_and_conquer_closest_pair(pl))
