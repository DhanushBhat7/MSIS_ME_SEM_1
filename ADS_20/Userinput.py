from sll import LinkedList
from dll import DoublyLinkedList


ll = LinkedList()
dll = DoublyLinkedList()

def sll_menu():


    while True:

        print("\n========== SLL MENU ==========")
        print("1. Insert")
        print("2. Insert End")
        print("3. Insert Middle")
        print("4. Display")
        print("5. Delete Beginning")
        print("6. Delete End")
        print("7. Delete Middle")
        print("8. Search")
        print("9. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            value = input("Enter value: ")
            ll.insert(value)

        elif choice == "2":

            value = input("Enter value: ")
            ll.insertend(value)

        elif choice == "3":

            value = input("Enter value: ")
            position = int(input("Enter position: "))
            ll.insertmid(value, position)

        elif choice == "4":

            ll.display()

        elif choice == "5":

            ll.delete()

        elif choice == "6":

            ll.deleteend()

        elif choice == "7":

            position = int(input("Enter position: "))
            ll.deletemid(position)

        elif choice == "8":

            value = input("Enter value to search: ")
            ll.search(value)

        elif choice == "9":

            break

        else:

            print("Invalid choice! Please try again.")


def dll_menu():

    while True:

        print("\n========== DLL MENU ==========")
        print("1. Insert Beginning")
        print("2. Insert End")
        print("3. Insert Middle")
        print("4. Display")
        print("5. Delete End")
        print("6. Delete Beginning")
        print("7. Delete Middle")
        print("8. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            value = input("Enter value: ")
            dll.insert(value)

        elif choice == "2":

            value = input("Enter value: ")
            dll.insertend(value)

        elif choice == "3":

            value = input("Enter value: ")
            position = int(input("Enter position: "))
            dll.insertmid(value, position)

        elif choice == "4":

            dll.display()

        elif choice == "5":

            dll.delete()

        elif choice == "6":

            dll.deletebegin()

        elif choice == "7":

            position = int(input("Enter position: "))
            dll.deletemid(position)

        elif choice == "8":

            break

        else:

            print("Invalid choice! Please try again.")


def main():


    while True:

        print("1. Singly Linked List")
        print("2. Doubly Linked List")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            sll_menu()

        elif choice == "2":

            dll_menu()

        elif choice == "3":

            print("Program terminated.")
            break

        else:

            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
