def Bubblesort(a):
    n=len(a)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if a[j]>=a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swapped = True
        if swapped == False:
            break
    return a

list = [3,2,4,5,2,1]
sorted = Bubblesort(list)
print(sorted)