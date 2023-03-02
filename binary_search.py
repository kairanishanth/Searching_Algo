#binary search O(1)in best O(logn) in avg and worst   
def binarysearch(arr,x,low,high):
    while low<=high:      
        mid=low+(high-low)//2    #finding out the mid element 
        if arr[mid]==x:
            return mid 
        elif arr[mid]<x:
            low=mid+1 
        else:
            high=mid-1
    return -1 
arr=[2,1,4,5,3,7,8,9]
x=9
print(binarysearch(arr,x,0,len(arr)-1))
    