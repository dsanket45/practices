# LINEAR SEARCH ALGORITHM--------------------------------------------------------=>
def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
          
arr=[8,6,3,1,2,4,5,7,9]
target=10

a=linearSearch(arr,target)
if a!=-1:
    print(f"Target {target} is found at index {a}")
else:
    print(f"Target {target} not found")
    



# BINARY SEARCH ALGORITHM-------------------------------------------------------------=>
# using recursion
def binary_search(arr,low,high,item):
    if low<=high:
        mid=(low+high)//2
        if item==arr[mid]:
            return f"item {arr[mid]} found at index {mid}"
        elif item < arr[mid]:
            return binary_search(arr,low,mid-1,item)  #calling function itself
        else:
            return binary_search(arr,mid+1,high,item)   #calling function itself
    else:
        return "not found"
    
arr=[1,2,3,4,5,6,7,8,9]
print(binary_search(arr,0,len(arr)-1,5))


# by swapping method
def bin_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if target==arr[mid]:
            print(f"item found at {mid}")
            # break
            return 
        elif target<arr[mid]:
            high=mid-1  #shifting high value to mid-1 
        else:
            low=mid+1   #shifting low value to mid+1
    # else:
    print("item not found")
        
arr=[1,2,3,4,5,6,7,8,9]
bin_search(arr,4)