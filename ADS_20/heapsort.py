def maxheap(arr,n,i):
    global swaps, iterations
    iterations+=1
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n  and arr[i]<arr [left]:
        largest = left

    if right< n and arr[i]<arr[right]:
        largest = right

    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]
        swaps=+1
        maxheap(arr,n,largest)


def heapsort(arr):
    global swaps, iterations
    swaps = 0
    iterations = 0
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        maxheap(arr,n,i)

    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        maxheap(arr,i,0)
        print(f"iteration{n-i}: {arr}")
    print("total Iterations: ",iterations)
    print("Total number of swaps: ",swaps)

arr = [9,2,5,3,7,8,10]
print(arr)
heapsort(arr)
print(arr)