# 0:bob
# 1:jim
# 2:tom

# 0:ann
# 1:lea
# 2:sue

n=3
men=[[1,0,2],[1,2,0],[2,1,0]]
women=[[1,2,0],[2,0,1],[1,2,0]]

def check(lst):
    for i in range(n):
        if lst[i]==-1:
            return i
    return "FALSE"

men_occ=[-1,-1,-1]
women_occ=[-1,-1,-1]

while True:
    i=check(men_occ)
    if i=='FALSE':
            break
    for j in men[i]:#men preference
        #occupied
        if women_occ[j]!=-1:
            cur_man=women_occ[j]
            wannabe_man=i
            lst=women[j] #women preference
            cur_pref=lst.index(cur_man)
            wannabe_pref=lst.index(wannabe_man)
            if wannabe_pref < cur_pref:
                women_occ[j]=wannabe_man
                men_occ[wannabe_man]=j
                men_occ[cur_man]=-1
                break
        # not occupied
        else:
            men_occ[i]=j
            women_occ[j]=i
            break


print(men_occ)

