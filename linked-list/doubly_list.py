class Node:
    def __init__(self, value: int, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self) -> None:
        self.length: int = 0
        self.head: Node = None
        self.tail: Node = None

    # O(1)
    def append(self, value: int) -> None:
        self.length += 1

        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    # O(1)
    def prepend(self, value: int) -> None:
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    # O(n)
    def insert(self, value: int, index: int) -> None:
        if index < 0:
            raise IndexError("Index cannot be negative value")

        if index == 0:
            self.prepend(value)
            return

        if index == self.get_size():
            self.append(value)
            return

        if index > self.get_size():
            raise IndexError("Index out of range")

        self.length += 1
        head = self.head
        for _ in range(index - 1):
            head = head.next

        new_node = Node(value, prev=head, next=head.next)
        if head.next:
            head.next.prev = new_node
        head.next = new_node

    # O(1)
    def insert_after(self, value: int, node: Node) -> Node:
        if not isinstance(node, Node):
            raise TypeError("node must be a valid Node instance")

        self.length += 1

        new_node = Node(value, next=node.next, prev=node)

        if node.next:
            node.next.prev = new_node

        node.next = new_node

        if node == self.tail:
            self.tail = new_node

        return new_node

    # O(1)
    def pop(self) -> int:
        if not self.tail:
            raise IndexError("Cannot pop from empty list")

        self.length -= 1

        value = self.tail.value

        if self.tail.prev is None:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return value

    # O(1)
    def unshift(self) -> int:
        if not self.head:
            raise IndexError("Cannot pop from empty list")

        self.length -= 1

        value = self.head.value

        if not self.head.next:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        return value

    # O(n)
    def remove(self, value: int, all: bool = False) -> None:
        if not self.head:
            raise IndexError("Cannot pop from empty list")

        head = self.head

        while head:
            if head.value == value:
                self.length -= 1

                if head == self.head:
                    self.head = head.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None

                elif head == self.tail:
                    self.tail = head.prev

                    if self.tail:
                        self.tail.next = None
                else:
                    head.prev.next = head.next
                    if head.next:
                        head.next.prev = head.prev

                if not all:
                    return

            head = head.next

    # O(n)
    def delete(self, index: int) -> None:
        if index < 0 or index >= self.get_size():
            raise IndexError("index out of range")

        self.length -= 1

        head = self.head
        current_index: int = 0

        while head:
            if current_index == index:
                if head == self.head:
                    self.head = head.next

                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif head == self.tail:
                    self.tail = head.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    head.prev.next = head.next
                    if head.next:
                        head.next.prev = head.prev

                return

            head = head.next
            current_index += 1

    # O(n)
    def search(self, value: int) -> Node:
        head = self.head

        while head:
            if head.value == value:
                return head
            head = head.next

        return False

    def get_size(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return self.get_size() == 0

    def traverse(self) -> None:
        print("Size: ", self.get_size())

        current_head = self.head

        forword: str = ""
        backword: str = ""

        while current_head:
            forword += f"{current_head.value} -> "
            backword += f" <- {current_head.prev.value}" if current_head.prev else "nil"

            current_head = current_head.next

        print(forword)
        print(backword)

    def __str__(self) -> str:
        head: str = f"{self.head.value}" if self.head else "None"
        tail: str = f"{self.tail.value}" if self.tail else "None"

        return f"Head: {head}, Tail: {tail}"


def main() -> None:
    ll = LinkedList()
    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)

    # ll.insert(100,6)
    # ll.pop()
    # ll.unshift()
    # ll.remove(0, True)
    ll.delete(6)

    ll.traverse()
    print(ll)


if __name__ == "__main__":
    main()
