class Node:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.length = 0
        self.head: Node = None
        self.tail: Node = None

    # O(1)
    def prepend(self, val: int) -> None:
        new_node = Node(val)

        self.length += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head

    # O(1)
    def append(self, val: int) -> None:
        new_node = Node(val)

        self.length += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.next = self.head
        self.tail = new_node


    # O(n)
    def pop(self) -> Node:
        if self.is_empty():
            return None

        head = self.head
        self.length -= 1

        while head:
            if head.next is self.tail:
                tail = self.tail
                head.next = None
                self.tail = head
                return tail

            head = head.next

    # O(1)
    def unshift(self) -> Node:
        if self.is_empty():
            return None

        self.length -= 1

        head = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return head

        self.head = self.head.next
        return head

    # O(n)
    def traverse(self) -> None:
        print("Length:", self.length)

        if self.is_empty():
            return

        print("HEAD:", self.head.val, "TAIL:", self.tail.val)

        result: str = ""

        head = self.head

        while head:
            result += f"{head.val} -> "

            if head == self.tail:
                break

            head = head.next

        print(result)

    def get_size(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return self.length == 0


def main() -> None:
    ll = LinkedList()
    ll.prepend(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.prepend(7)
    ll.pop()
    ll.unshift()
    ll.unshift()
    ll.unshift()
    ll.unshift()

    ll.traverse()


if __name__ == "__main__":
    main()
