
class node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedlist: 
    def __init__(self, head=None):
        self.head = head

    def print_ll(self, input): 
        if (input.head == None): 
            print("[]")
        else: 
            print("[")
            print (input.head.value)
            current = input.head
            while current.next != None:
                current = current.next
                print (current.value)
            print("]")
            print("\n")

    def append(self, value):
        if (self.head == None): 
            self.head = node(value)
        else: 
            current = self.head
            while current.next != None: 
                current = current.next
            current.val = node(value)
            
    def pop(self): 
        if self.head is None: 
            return None
        if self.head.next is None:
            temp = self.head.value
            self.head = None
            return value
        
        current = self.head
        while current.next.next: 
            current = current.next
        value = current.next.value
        current.next = None
        return value

    def peek(self): 
        if self.head is None: 
            return None
        current = self.head
        while current.next: 
            current = current.next
        return current.value

    def remove(self, value): 
        if self.head is None: 
            return None

        if self.head.next is None: 
            if self.head.value == value: 
                self.head = None
                return True
            return None

        if self.head.next.next is None: 
            if self.ehad.next.value == value: 
                self.head.next = None
                return True

        current = self.head
        while current.next.next: 
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next
        return None

    def insert_first(self, value): 
        next_node = self.head
        self.head = Node(value) 
        self.head.next = next_element

    def delete_first(self):
        if self.head: 
            new = self.head.next
            self.head = new

class treeNode: 
    def __init__(self, value, left, right): 
        self.val = value
        self.left = left
        self.right = right

list = linkedlist()
list.append(1)
list.print_ll(list)
list.append(2)
list.print_ll(list)
list.append(3)
print(list)




