def selectionsort(a):
    n=len(a)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min=j
        a[i],a[min] = a[min],a[i]
        print(f"after {i+1} iterations")
        print(a)
    return a

list=[65,32,28,9,10,2,33]
print(list)
sorted = selectionsort(list)



    