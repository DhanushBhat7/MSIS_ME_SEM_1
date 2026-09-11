from sll import LinkedList,node
from dll import DoublyLinkedList,node
from stack import Stack
from queue import queue


# ==============================
# SINGLY LINKED LIST MENU
# ==============================
def sll_menu():
    while True:
        print("\n========== SLL MENU ==========")
        print("1. Insert")
        print("2. Insert End")
        print("3. Insert Middle")
        print("4. Display")
        print("5. Delete")
        print("6. Delete End")
        print("7. Delete Middle")
        print("8. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            value = input("Enter value: ")
            LinkedList.insert(value)

        elif choice == "2":
            value = input("Enter value: ")
            LinkedList.insertend(value)

        elif choice == "3":
            value = input("Enter value: ")
            position = int(input("Enter position: "))
            LinkedList.insertmid(value, position)

        elif choice == "4":
            LinkedList.display()

        elif choice == "5":
            value = input("Enter value to delete: ")
            LinkedList.delete(value)

        elif choice == "6":
            LinkedList.deleteend()

        elif choice == "7":
            position = int(input("Enter position: "))
            LinkedList.deletemid(position)

        elif choice == "8":
            break

        else:
            print("Invalid choice!")


def dll_menu():
    while True:
        print("\n========== DLL MENU ==========")
        print("1. Insert")
        print("2. Insert End")
        print("3. Insert Middle")
        print("4. Display")
        print("5. Delete")
        print("6. Delete End")
        print("7. Delete Middle")
        print("8. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            value = input("Enter value: ")
            DoublyLinkedList.insert(value)

        elif choice == "2":
            value = input("Enter value: ")
            DoublyLinkedList.insertend(value)

        elif choice == "3":
            value = input("Enter value: ")
            position = int(input("Enter position: "))
            DoublyLinkedList.insertmid(value, position)

        elif choice == "4":
            DoublyLinkedList.display()

        elif choice == "5":
            value = input("Enter value to delete: ")
            DoublyLinkedList.deletebegin(value)

        elif choice == "6":
            DoublyLinkedList.delete()

        elif choice == "7":
            position = int(input("Enter position: "))
            DoublyLinkedList.deletemid(position)

        elif choice == "8":
            break

        else:
            print("Invalid choice!")


def stack_menu():
    while True:
        print("\n========== STACK MENU ==========")
        print("1. Append")
        print("2. Pop")
        print("3. Display")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            value = input("Enter value: ")
            Stack.append(value)

        elif choice == "2":
            Stack.pop()

        elif choice == "3":
            Stack.display()

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


def queue_menu():
    while True:
        print("\n========== QUEUE MENU ==========")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            value = input("Enter value: ")
            queue.push(value)

        elif choice == "2":
            queue.pop()

        elif choice == "3":
            queue.display()

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


def main():
    while True:
        print("\n================================")
        print("     DATA STRUCTURE PROGRAM")
        print("================================")
        print("1. Singly Linked List (SLL)")
        print("2. Doubly Linked List (DLL)")
        print("3. Stack")
        print("4. Queue")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sll_menu()

        elif choice == "2":
            dll_menu()

        elif choice == "3":
            stack_menu()

        elif choice == "4":
            queue_menu()

        elif choice == "5":
            print("Program terminated.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
