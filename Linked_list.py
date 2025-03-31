class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += str(current.value)
            if current.next: 
                result += " -> "
            current = current.next
        return result
    


    def insert_at_head(self, value):
        node = LinkedListNode(value)
        node.next = self.head
        self.head = node


    
    def minimum(self):
        if not self.head:
            return None  
        aus = self.head
        current_min = aus.value
        while aus:
            if aus.value < current_min:
                current_min = aus.value
            aus = aus.next
        return current_min
    

    
    def maximum(self):
        if not self.head:
            return None  
        aus = self.head
        current_max = aus.value
        while aus:
            if aus.value > current_max:
                current_max = aus.value
            aus = aus.next
        return current_max
    

    
    def successor(self, value):
        aus = self.head
        succ = None
        while aus:
            if aus.value > value:
                if succ is None or aus.value < succ.value:
                    succ = aus
            aus = aus.next
        return succ
    


    def predecessor(self, value):
        aus = self.head
        prec = None
        while aus:
            if aus.value < value:
                if prec is None or aus.value > prec:
                    prec = aus.value
            aus = aus.next
        return prec
    
    
    
    def search(self, value):
        aus = self.head
        while aus:
            if aus.value == value:
                return aus
            aus = aus.next
        return None  