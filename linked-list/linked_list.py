class Node:
    def __init__(self, data: int, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None

    # O(1)
    def prepend(self, value: int) -> None:
        head = self.head
        self.length += 1
        new_node: Node = Node(data=value)

        if head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = head
            self.head = new_node

    # O(n) if not tail pointer else O(1)
    def append(self, value: int) -> None:
        self.length += 1
        new_node: Node = Node(data=value)

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node

    # O(n)
    def insert(self, value: int, index: int) -> None:
        if index < 0:
            raise IndexError("Index cannot be negative value")

        if index == 0:
            self.prepend(value)
            return

        if index == self.get_length():
            self.append(value)
            return

        if index > self.get_length():
            raise IndexError("Index out of range")

        head = self.head
        new_node = Node(data=value)
        self.length += 1

        for _ in range(index - 1):
            head = head.next

        new_node.next = head
        head.next = new_node

    # O(1)
    def insert_after(self, value: int, node: Node = None) -> None:
        if not node or not isinstance(node, Node):
            raise TypeError("node must be a valid Node instance")

        self.length += 1

        new_node = Node(value, node.next)
        node.next = new_node

        if new_node.next is None:
            self.tail = new_node

    # O(n)
    def pop(self) -> int:
        if not self.head:
            raise IndexError("Cannot pop from empty list")

        head = self.head

        if head == self.tail:
            value = head.data
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        while head.next != self.tail:
            head = head.next

        value = self.tail.data

        head.next = None
        self.tail = head
        self.length -= 1

        return value

    # O(1)
    def unshift(self) -> None:
        if self.head is None:
            return

        self.length -= 1
        self.head = self.head.next

        if self.head is None:
            self.tail = None

    # O(n)
    def remove(self, value: int, all: bool = False) -> None:
        if not self.head:
            return

        while self.head and self.head.data == value:
            self.length -= 1
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            if not all:
                return

        head = self.head

        while head and head.next:
            if head.next.data == value:
                self.length -= 1
                head.next = head.next.next

                if head.next is None:
                    self.tail = head

                if not all:
                    return
            else:
                head = head.next

    # O(n)
    def delete(self, index: int = 0) -> None:

        if index < 0:
            raise IndexError("Index cannot be negative value")

        if index >= self.get_length():
            raise IndexError("Index range exceeded")

        self.length -= 1

        if index == 0:
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return

        current_index: int = 0
        head = self.head

        while head and head.next:

            if current_index == index - 1:
                if head.next == self.tail:
                    self.tail = head

                head.next = head.next.next
                return

            head = head.next
            current_index += 1

    # O(n)
    def search(self, value: int) -> Node:
        head = self.head

        while head:
            if head.data == value:
                return head

            head = head.next

        return None

    # O(n)
    def traverse(self) -> None:
        head = self.head

        data: str = ""
        while head:
            data += f"{head.data} -> "
            head = head.next

        print(data)

    def get_length(self) -> int:
        return self.length

    def __str__(self) -> str:
        head = str(self.head.data) if self.head else "None"
        tail = str(self.tail.data) if self.tail else "None"
        return f"Head: {head}, Tail: {tail}"


linked_list = LinkedList()


def main() -> None:
    linked_list.prepend(0)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(6)
    linked_list.insert(7, 0)
    linked_list.remove(8, True)
    linked_list.delete(6)

    print(linked_list)

    print("Length:", linked_list.get_length())
    linked_list.traverse()


if __name__ == "__main__":
    main()
