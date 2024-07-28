import copy
class bf:
    def __init__(self):
        #self.lst=[[1,2,6],[1,3,5],[1,4,5],[2,5,-1],[3,2,-2],[3,5,1],[4,3,-2],[4,6,-1],[6,7,3],[5,7,3]]
        self.lst=[[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]]
        self.n=6
        # assuming source is 0 node
        self.mc=[0,float('inf'),float('inf'),float('inf'),float('inf'),float('inf')]

    def rs(self):
        mc=copy.deepcopy(self.mc)
        for i in range((self.n)-1): 
            for j in range(len(self.lst)): # edges
                u=self.lst[j][0]
                v=self.lst[j][1]
                d_uv=self.lst[j][2]
                d_u=mc[u]
                d_v=mc[v]
                if d_u + d_uv < d_v :
                    mc[v]=d_u+ d_uv
            #print('j',mc)

        print(mc)



bf=bf()
bf.rs()


