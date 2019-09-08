def selection_sort(lst):
    for i, e in enumerate(lst):
        #print(lst.__getitem__)
        mn = min(range(i,len(lst)), key=lst.__getitem__)#returns the index of the minim number
        print(mn)
        lst[i], lst[mn] = lst[mn], e
    return lst
print(selection_sort([2,4,1,3,5]))