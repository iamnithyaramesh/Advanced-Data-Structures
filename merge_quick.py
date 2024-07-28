def merge(l1, l2):
    merged_list=[]
    i=j=0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i+=1
        else:
            merged_list.append(l2[j])
            j+=1

    while i < len(l1):
        merged_list.append(l1[i])
        i+=1

    while j < len(l2):
        merged_list.append(l2[j])
        j+=1

    return merged_list

def merge_sort(lst):
    if len(lst)<2:
        return lst
    else:
        n=len(lst)//2
        lsorted=merge_sort(lst[:n])
        rsorted=merge_sort(lst[n:])
        return merge(lsorted,rsorted)
    
def partition(l,low,high):
    pivot=l[high]
    i=low-1
    for j in range(low, high):
        if l[j] <= pivot:
            i = i + 1
            (l[i],l[j]) = (l[j],l[i])
    (l[i+1],l[high]) = (l[high], l[i + 1])
    return i+1

def quick_sort(lst,low,high):
    if low<high:
        pi=partition(lst, low, high)
        quick_sort(lst, low, pi - 1)
        quick_sort(lst, pi + 1, high)

if __name__=='__main__':
    l=[55,7,77,3,4,1,0,29,14]
    print("Using merge sort:",merge_sort(l))
    quick_sort(l,0,len(l)-1)
    print("Using quick sort:",l)