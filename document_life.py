class Node:
    def __init__(self, year, highlight, next = None):
        self.year = year
        self.highlight = highlight
        self.next = next

    def get_year(self):
        return self.year

    def get_highlight(self):
        return self.highlight

    def get_next(self):
        return self.next

    def set_year(self, year):
        self.year = year

    def set_highlight(self, highlight):
        self.highlight = highlight

    def set_next(self, next):
        self.next = next

class LinkedList:
    def __init__(self, year, highlight):
        self.head = Node(year, highlight)

    def get_head(self):
        return self.head

    def insert_start(self, year, highlight):
        new_node = Node(year, highlight)
        new_node.set_next(self.head)
        self.head = new_node

    def get_data(self):
        current_node = self.get_head()
        while current_node:
            if current_node.get_year() != None:
                print(f"{current_node.get_year()} - {current_node.get_highlight()}")
            current_node = current_node.get_next()


document_life = LinkedList(7, "I knew I will be a codder")
document_life.insert_start(2, "I Strated talking and saying I'm going to be a codder")
document_life.insert_start(0, "A codder is born")

current_node = document_life.get_head()
age = int(input("How old are you? "))

while current_node.get_year() < age:
    current_age = current_node.get_year() + 1
    if current_node.get_next() != None and current_node.get_next().get_year() == current_age:
        current_node = current_node.get_next()
    else:
        highlight = input(f"What is the highlight of year {current_age}: ")
        new_node = Node(current_age, highlight, current_node.get_next())
        current_node.set_next(new_node)
        current_node = new_node



document_life.get_data()
