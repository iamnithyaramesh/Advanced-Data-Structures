'''def kruskals(vertices, edges):
    mst = []
    union=set()
    sorted_edges = sorted(edges.items(), key=lambda x: x[1])

    for edge, weight in sorted_edges:
        u,v = edge
        if u not in union or v not in union:
            mst.append((edge, weight))
            union.add(u)
            union.add(v)

    return mst

print(kruskals([1,2,3,4,5],{(1,2):1,(2,1):1,(2,3):2,(2,4):1,(3,4):7,(1,4):1,(3,4):2,(1,3):2,(3,5):11,(1,5):17}))'''




 


    