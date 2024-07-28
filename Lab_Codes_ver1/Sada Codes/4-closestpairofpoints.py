import math

def distance(p, q):
    return math.sqrt(math.pow(p[0] - q[0], 2) + math.pow(p[1] - q[1], 2))

def minDistanceRec(Px, Py):
    s = len(Px)
    if s == 2:
        return distance(Px[0], Px[1]), (Px[0], Px[1])
    elif s == 3:
        d1 = distance(Px[0], Px[1])
        d2 = distance(Px[1], Px[2])
        d3 = distance(Px[2], Px[0])
        min_distance = min(d1, d2, d3)
        if min_distance == d1:
            min_pair = (Px[0], Px[1])
        elif min_distance == d2:
            min_pair = (Px[1], Px[2])
        else:
            min_pair = (Px[2], Px[0])
        return min_distance, min_pair
    
    #[(1, 2), (3, 5), (6, 9), (8, 12), (10, 15)]
    m = s // 2
    Qx = Px[:m] #[(1, 2), (3, 5)]
    Rx = Px[m:] #[(6, 9), (8, 12), (10, 15)]]
    xR = Rx[0][0] #6
    Qy = []
    Ry = []
    for p in Py:
        if p[0] < xR:
            Qy.append(p)
        else:
            Ry.append(p)
    
    delta1, pair1 = minDistanceRec(Qx, Qy)
    delta2, pair2 = minDistanceRec(Rx, Ry)
    delta = min(delta1, delta2)
    if delta1 < delta2:
        min_pair = pair1
    else:
        min_pair = pair2
    
    Sy = [p for p in Py if abs(p[0] - xR) <= delta]
    sizeS = len(Sy)
    if sizeS > 1:
        minS = distance(Sy[0], Sy[1])
        minPair = (Sy[0], Sy[1])
        for i in range(1, sizeS - 1):
            for j in range(i, min(i + 15, sizeS - 1)):
                d = distance(Sy[i], Sy[j + 1])
                if d < minS:
                    minS = d
                    minPair = (Sy[i], Sy[j + 1])
        return min(delta, minS), minPair
    else:
        return delta, min_pair

def minDistance(Points):
    Px = sorted(Points)
    Py = sorted(Points, key=lambda x: x[1])
    minDist, minPair = minDistanceRec(Px, Py)
    return round(minDist, 2), minPair

pts = [(1, 2), (3, 5), (6, 9), (8, 12), (10, 15)]
result, pair = minDistance(pts)
print(f"Minimum Distance: {result}, Pair: {pair}")
