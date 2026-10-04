def insertionsort(a):
    n=len(a)
    for i in range(n):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1] = a[j]
            j-=1
        a[j+1]=key
        print(f"after {i} iterations")
        print(a)
    return a


list=[65,32,28,9,10,2,33]
print(list)
sorted = insertionsort(list)