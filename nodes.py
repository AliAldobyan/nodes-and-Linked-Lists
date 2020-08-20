class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self, data=None):
        self.head_node = Node(data)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def get_data(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_data() != None:
                string_list += str(current_node.get_data()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, data):
        current_node = self.get_head_node()
        if current_node.get_data() == data:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_data() == data:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node


r2d2 = LinkedList(2)
r2d2.insert_beginning("D")
r2d2.insert_beginning(2)
r2d2.insert_beginning("D")
r2d2.insert_beginning("R")
r2d2.insert_beginning(2)
r2d2.remove_node(2)
r2d2.remove_node("R")

print(r2d2.get_data())
