def BinarySearch(arr,low,high,key):
    n=len(arr)
    mid = (low+high)/2

    if arr[mid] == key:
        return print("Key is found!!")
    elif arr[mid] > key :
        BinarySearch(arr,low,mid,key)
    elif arr[mid] < key:
        BinarySearch(arr,mid+1,high,key)
    else:
        return print("key is not in the list !!")

def linearsearch(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return print(f"the {key} is found at position {i}")
        else:
            return print("key Not found")


arr=[2,5,1,7,4,9,12,4,5,6,2,70,64,53,64]

key = 5

print(BinarySearch(arr,0,len(arr),key))
print(linearsearch(arr,key))