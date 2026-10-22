from mergesort import mergesort
from quicksort import quicksort
from bubblesort import Bubblesort
from selectionsort import selectionsort
from insertionsort import insertionsort


def main():
    arr = list(map(int, input("Enter space-separated elements: ").split()))
    print("Array:", arr)

    while True:
        print("\n========== Sort MENU ==========")
        print("1. merge")
        print("2. quick")
        print("3. bubble")
        print("4. selection")
        print("5. insertion")

        choice = int(input("Enter the sort choice: "))
        if choice == 1:
            sorted = mergesort(arr)
            print(sorted)
            break

        elif choice == 2:
            n=len(arr)
            sorted = quicksort(arr,0,n-1)
            print(sorted)
            break

        elif choice == 3:
            sorted = Bubblesort(arr)
            print(sorted)
            break

        elif choice == 4:
            sorted = selectionsort(arr)
            print(sorted)
            break

        elif choice == 5:
            sorted = insertionsort(arr)
            print(sorted)
            break

        else:
            print("Inavlid Input !!")
    

if __name__ == "__main__":
    main()