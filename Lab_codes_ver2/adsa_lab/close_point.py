import random

import matplotlib.pyplot as plt


def mat(points):

    # Extract x and y coordinates from the list of tuples
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Plot the points
    plt.plot(x_values, y_values, marker='o', linestyle='', markersize=8, label='Points')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot of Points')
    plt.grid(True)
    plt.legend()
    plt.show()


def create(n):
    l=[]
    for i in  range(1,n+1):
        #a=eval(input(f'Enter the point in tuple {i}'))
        while True:
            a1=random.randrange(0,10)
            a2=random.randrange(0,10)
            a=(a1,a2)
            if a in l:
                continue
            else:
                break
        l.append(a)
    print(l)
    return l

def distance(tup1,tup2):
        return ((tup1[0]-tup2[0])**2+(tup1[1]-tup2[1])**2)**(0.5)
           


class ClosePoint:
    def __init__(self,lst):
        self.lst=lst
           
    def sort_point_x(self,lst):
        lst=sorted( self.lst,key =  lambda x : x[0])
        return lst
    
    def sort_point_y(self,lst):
        lst=sorted( lst,key =  lambda x : x[1])
        return lst
    

    def closest_pair(self,lst):
        n=len(lst)
        if n==2:
            return distance(lst[0],lst[1])
        elif n==3:
            return min(distance(lst[0],lst[1]),distance(lst[0],lst[2]),distance(lst[1],lst[2]))

        
        mid=n//2
        dl=self.closest_pair(lst[0:mid])
        dr=self.closest_pair(lst[mid:])
        d=min(dl,dr)


        ylst=self.sort_point_y(lst)

        up=ylst[mid][0]+d
        low=ylst[mid][0]-d

        ylst=[i for i in ylst if i[0]<up and i[0]>low ]

        y1len=len(ylst)

        if y1len<6:
            y2len=y1len
        else: 
            y2len=6

        for i in range(y1len):
            for j in range(y2len):
                if i==j:
                    continue
                else:  
                    d= min(d,distance(ylst[i],ylst[j]))

        return d


if __name__=="__main__":
    n=int(input('Enter the no. of points'))
    lst=create(n)
    # mat(lst)
    cp=ClosePoint(lst)
    print(cp.closest_pair(cp.sort_point_x(cp.lst)))
    



