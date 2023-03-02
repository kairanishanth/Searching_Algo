#linersearch O(n)
def linearsearch(arr,n,x):
    for i in range(n):
        if arr[i]==x:
            return i
    return -1 
arr=[1,2,5,3,4,8]
n=len(arr)
x=2
print(linearsearch(arr,n,x))