class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add a new node at the beginning.
    def add_head(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # Add a new node at the end.
    def add_tail(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    # Delete the first node.
    def delete_head(self):
        if self.head:
            self.head = self.head.next

    # Delete the last node.
    def delete_tail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    # Insert a node immediately after the first matching value.
    def add_after(self, target, data):
        current = self.head
        while current and current.data != target:
            current = current.next
        if current:
            node = Node(data)
            node.next = current.next
            current.next = node

    # Delete the node immediately after the first matching value.
    def delete_after(self, target):
        current = self.head
        while current and current.data != target:
            current = current.next
        if current and current.next:
            current.next = current.next.next

    # Return whether the value exists in the list.
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    # Return all list values as a Python list.
    def values(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    # Return a new list containing values common to both lists.
    def common(self, other):
        other_values = set(other.values())
        result = LinkedList()
        current = self.head
        while current:
            if current.data in other_values:
                result.add_tail(current.data)
            current = current.next
        return result

    # Find the sum of the last n nodes in one traversal.
    def sum_last_n(self, n):
        if n <= 0:
            return 0
        last_values = []
        total = 0
        current = self.head
        while current:
            last_values.append(current.data)
            total += current.data
            if len(last_values) > n:
                total -= last_values.pop(0)
            current = current.next
        return total

    # Reverse the linked list in place.
    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    # Split the list into two lists containing alternate nodes.
    def split_alternate(self):
        first = LinkedList()
        second = LinkedList()
        current = self.head
        use_first = True
        while current:
            next_node = current.next
            if use_first:
                first.add_tail(current.data)
            else:
                second.add_tail(current.data)
            use_first = not use_first
            current = next_node
        self.head = None
        return first, second

    # Check whether the linked list reads the same forwards and backwards.
    def is_palindrome(self):
        values = self.values()
        return values == values[::-1]

    # Remove duplicate values while keeping their first occurrence.
    def remove_duplicates(self):
        seen = set()
        current = self.head
        previous = None
        while current:
            if current.data in seen:
                previous.next = current.next
            else:
                seen.add(current.data)
                previous = current
            current = current.next

    # Find the middle node using slow and fast pointers.
    def middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    # Remove odd-valued nodes from a circular linked list.
    def remove_odd_circular(self):
        if self.head is None:
            return
        count = 1
        tail = self.head
        while tail.next != self.head:
            tail = tail.next
            count += 1
        previous = tail
        current = self.head
        for _ in range(count):
            next_node = current.next
            if current.data % 2 != 0:
                if current == self.head:
                    self.head = next_node
                previous.next = next_node
            else:
                previous = current
            current = next_node
        if self.head and self.head.data % 2 != 0:
            self.head = None

    # Detect a cycle using Floyd's slow and fast pointer method.
    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # Make the last node point back to the head.
    def make_circular(self):
        if self.head is None:
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = self.head


# Demonstrate all the linked-list operations.
if __name__ == "__main__":
    ll = LinkedList()
    ll.add_head(20)
    ll.add_head(10)
    ll.add_tail(30)
    ll.add_tail(40)
    print("Add head and tail:", ll.values())
    ll.delete_head()
    ll.delete_tail()
    print("   Delete head and tail:", ll.values())
    ll.add_after(20, 25)
    print("   Add after 20:", ll.values())
    ll.delete_after(20)
    print("   Delete after 20:", ll.values())
    print("   Search 30:", ll.search(30))

    a = LinkedList()
    b = LinkedList()
    for x in [1, 2, 3, 4]:
        a.add_tail(x)
    for x in [3, 4, 5, 6]:
        b.add_tail(x)
    print("Common elements:", a.common(b).values())

    print("Sum of last 3 nodes:", a.sum_last_n(3))

    reverse_list = LinkedList()
    for x in [1, 2, 3, 4]:
        reverse_list.add_tail(x)
    reverse_list.reverse()
    print("Reversed list:", reverse_list.values())

    split_list = LinkedList()
    for x in [1, 2, 3, 4, 5]:
        split_list.add_tail(x)
    left, right = split_list.split_alternate()
    print("Alternate split:", left.values(), "and", right.values())

    palindrome_list = LinkedList()
    for x in [1, 2, 3, 2, 1]:
        palindrome_list.add_tail(x)
    print("Is palindrome:", palindrome_list.is_palindrome())

    duplicate_list = LinkedList()
    for x in [1, 2, 2, 3, 1]:
        duplicate_list.add_tail(x)
    duplicate_list.remove_duplicates()
    print("After removing duplicates:", duplicate_list.values())

    middle_list = LinkedList()
    for x in [10, 20, 30, 40, 50]:
        middle_list.add_tail(x)
    print("Middle element:", middle_list.middle())

    circular_list = LinkedList()
    for x in [1, 2, 3, 4, 5, 6]:
        circular_list.add_tail(x)
    circular_list.make_circular()
    circular_list.remove_odd_circular()
    # Print circular values without following the cycle forever.
    circular_values = []
    current = circular_list.head
    if current:
        start = current
        while True:
            circular_values.append(current.data)
            current = current.next
            if current == start:
                break
    print("Circular list after removing odd values:", circular_values)

    cycle_list = LinkedList()
    for x in [1, 2, 3]:
        cycle_list.add_tail(x)
    cycle_list.make_circular()
    print("Contains cycle:", cycle_list.has_cycle())
