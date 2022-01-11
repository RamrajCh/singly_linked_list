class Node:
    # Initialize node with element and reference to next node
    def __init__(self, element, next) -> None:
        self.element = element
        self.next = next


class SinglyLinkedList:
    # function to initialize head and tail to None
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    

    # function to check if list is empty
    def is_empty(self) -> bool:
        return not self.head
    

    # function to insert node at head
    def add_to_head(self, data) -> None:
        newNode = Node(element=data, next=self.head)
        self.head = newNode
        if self.tail is None:
            self.tail = self.head

    
    # function to insert node at tail
    def add_to_tail(self, data) -> None:
        newNode = Node(element=data, next=None)
        if self.is_empty():
            self.add_to_head(data)
        else:
            self.tail.next = newNode
            self.tail = newNode


    # function to insert node after a predecessor node
    def add_after(self, predecessor:Node, data) -> None:
        if type(predecessor) is not Node:
            print("predecessor must be an instance of type SinglyLinkedList")
        else:
            newNode = Node(element=data, next=predecessor.next)
            predecessor.next = newNode


    # function to remoe node from head
    def remove_from_head(self) -> None:
        if self.is_empty():
            print("No node to delete")
        else:
            node_to_remove = self.head
            self.head = node_to_remove.next
            del node_to_remove
    

    # function to remove first occurance of data
    def remove(self, data) -> None:
        if self.is_empty():
            print("No node to delete")
            return
        if self.head.element == data:
            self.remove_from_head()
            if self.head is None:
                self.tail = None
            return
        else:
            temp = self.head.next
            prev = self.head
            while temp:
                if temp.element == data:
                    prev.next = temp.next
                    temp = None
                    if prev.next is None:    # if the node being deleted is last node
                        self.tail = prev
                    return
                else:
                    prev = prev.next
                    temp = temp.next
            print("Node was not found!")

    
    # function to search node in list; returns true if found
    def search(self, data) -> bool:
        current = self.head
        while current:
            if current.element == data:
                return True
            else:
                current = current.next
        return False


    # function to traverse list
    def print_list(self) -> None:
        if self.is_empty():
            print("List is empty")
        else:
            temp = self.head
            while (temp):
                print(temp.element)
                temp = temp.next
        print("-"*30)

if __name__ == '__main__':
    S = SinglyLinkedList()

    S.add_to_head(3)
    S.add_to_tail(10)
    S.add_to_tail(30)
    S.add_to_head(34)
    S.add_after(S.head.next, 23) # add after next of head of S
    S.add_after(S.head, 12)  # add after head of S
    
    S.print_list()

    S.remove_from_head()

    S.print_list()

    S.remove(12)

    S.print_list()

    print(S.search(34))
