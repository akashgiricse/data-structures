class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_the_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return

        curr_node = self.head

        while curr_node.next:
            curr_node = curr_node.next

        node = Node(data, None)
        curr_node.next = node

    def create_ll_from_array(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_the_end(data)

    def get_length(self):
        len = 0
        itr = self.head
        while itr:
            len += 1
            itr = itr.next

        return len

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        curr_index = 0
        itr = self.head
        while itr:
            if curr_index + 1 == index:
                itr.next = itr.next.next
                return
            curr_index += 1
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        node = Node(data, None)
        if index == 0:
            temp = self.head
            self.head = node
            node.next = temp
            return
        curr_index = 0
        itr = self.head
        while itr:
            if curr_index + 1 == index:
                temp = itr.next
                itr.next = node
                node.next = temp
                return
            itr = itr.next
            curr_index += 1

    def delete_by_value(self, value):
        pass

    def print(self):
        itr = self.head
        if self.head is None:
            print("Empty linked list")
            return
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"

            itr = itr.next

        print(llstr[:-3])


if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(10)
    # ll.insert_at_the_end(100)
    # ll.insert_at_the_end(1005)
    ll.create_ll_from_array(["Akash", "Giri", "is", "not", "cool."])
    ll.print()
    print(ll.get_length())
    ll.remove_at(3)
    ll.print()
    print(ll.get_length())
    ll.insert_at(0, "Mr")
    ll.print()
    print(ll.get_length())
    ll.insert_at(4, "very")
    ll.print()
    print(ll.get_length())
