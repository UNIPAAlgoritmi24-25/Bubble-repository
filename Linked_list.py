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
        current = self.head
        succ = None
        while current:
            if current.value > value:
                if succ is None or current.value < succ.value:
                    succ = current
            current = current.next
        return succ
    


    def predecessor(self, value):
        current = self.head
        prec = None
        while current:
            if current.value < value:
                if prec is None or current.value > prec:
                    prec = current.value
            current = current.next
        return prec
    
    
    
    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current  
            current = current.next
        return None  



ll = LinkedList()
ll.insert_at_head(5)
ll.insert_at_head(10)
ll.insert_at_head(3)
ll.insert_at_head(7)
print("Ll:", ll)  


node = ll.search(10)
print("Node with value:", node)
print("Minimum value:", ll.minimum())  
print("Maximum value:", ll.maximum())  


succ_node = ll.successor(5)
print("Successor:", succ_node)

prec_value = ll.predecessor(5)
print("Predecessor of 5:", prec_value)  



ll2 = LinkedList()
ll2.insert_at_head("pippo")
ll2.insert_at_head("paperino")
ll2.insert_at_head("pluto")
ll2.insert_at_head("clarabella")

print ("LL2:",ll2)
print("Pippo's successor:",ll2.successor("pippo"))
print("Pippo's predecessor:",ll2.predecessor("pippo"))
print("Clarabella's predecessor:",ll2.predecessor("clarabella"))
print ("Minimum:", ll2.minimum())


ll3 = LinkedList()
ll3.insert_at_head(4.1)
ll3.insert_at_head(2.3)
ll3.insert_at_head(5.7)
ll3.insert_at_head(8.2)
ll3.insert_at_head(-5.2)
print ("ll3:",ll3)
print("minimum:",ll3.minimum())