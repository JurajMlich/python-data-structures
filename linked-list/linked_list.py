class Node:
    def __init__(self, value, next_node=None) -> None:
        self.value = value
        self.next = next_node


class LinkedList:
    """ A class used to represent a classic linked list """

    def __init__(self, *items):
        """
        :param items: items to insert into the list
        """
        self.__head = None
        self.__tail = None
        self.__size = 0

        for item in items:
            self.insert_at_end(item)

    def insert_at_end(self, item):
        """
        Insert an item at the end of the list.
        :param item: the item to insert
        """
        node = Node(item)

        if self.__head is None:
            self.__head = node

        if self.__tail is not None:
            self.__tail.next = node

        self.__tail = node
        self.__size += 1

    def insert_at_start(self, item):
        """
        Insert an item at the beginning of the list.
        :param item: the item to insert
        """
        node = Node(item)

        if self.__head is None:
            self.__head = node
            self.__tail = item
        else:
            node.next = self.__head
            self.__head = node

        self.__size += 1

    def delete(self, item):
        """
        Delete item from the list (even if included multiple times)
        :param item: item to delete
        """
        if self.__size == 0:
            return

        tail = self.__head
        current = self.__head.next

        while current is not None:
            if current.value == item:
                self.__size -= 1
            else:
                tail.next = current
                tail = current

            current = current.next

        if current != tail:
            tail.next = None

        self.__tail = tail

        if self.__head.value == item:
            self.pop()

    def delete_at(self, index):
        """
        Delete item at index
        :param index:
        """
        if index < 0:
            raise IndexError

        if index > self.__size - 1:
            raise IndexError

        previous_node = self.__head

        for i in range(index - 1):
            previous_node = previous_node.next

        previous_node.next = previous_node.next.next

        if previous_node.next is None:
            self.__tail = previous_node

        self.__size -= 1

    def __iter__(self):
        current_node = self.__head
        while current_node:
            yield current_node.value
            current_node = current_node.next

    def pop(self):
        """
        Delete first item
        """
        if self.__size == 0:
            raise IndexError

        self.__head = self.__head.next

    def reverse(self):
        """
        Reverse the list
        :return: the reversed list
        """

        if self.size == 0:
            return

        tail = Node(self.__head.value)
        head = tail
        current = self.__head

        while current.next is not None:
            new = Node(current.next.value)
            new.next = head
            head = new
            current = current.next

        self.__head = head
        self.__tail = tail

    @property
    def size(self):
        return self.__size
