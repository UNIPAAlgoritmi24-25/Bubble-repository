
class LinkedListNode:
    def __init__ (self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    #def  __str__ (self):
        #return ( "Node with value: " + str(self.value) + "\nNext:"+ str(self.next))
    



class LinkedList:
    def __init__ (self, head = None):
        self.head = head

    
    def __str__ (self): # avvalersi di una struttura ausiliaria per raccogliere i Nodi e fare un join?    
        pass


    def insert_at_head(self, value):
        node = LinkedListNode(value)
        node.next = self.head
        self.head = node


    def minimum (self):
        pass


    def maximum (self):
        pass


    def successor (self, value):
        current = self.head
        succ = None
        while current!= None:
            if current.value > value:
                if succ is None or current.value < succ.value:
                    succ = current
            current = current.next
        return succ
    

    
    def predecessor (self,value):
        current = self.head
        prec = None
        while current != None:
            if current.value < value:
                if prec is None or current.value > prec:
                    prec = current.value
            current = current.next
        return prec

    





    
    def minimum(self):
        if not self.values_list:
            return None
        
        min_value = self.values_list[0]
        for value in self.values_list:
            if value < min_value:
                min_value = value
        
        return min_value

    def maximum(self):
        if not self.values_list:
            return None
            
        max_value = self.values_list[0]
        for value in self.values_list:
            if value > max_value:
                max_value = value
            
        return max_value
    



ll = LinkedList()
ll.insert_at_head(2)
ll.insert_at_head(10)
ll.insert_at_head(5)


print(ll.predecessor(10))
print(ll.predecessor(5))
print(ll.successor(2))




ll2 = LinkedList()
ll2.insert_at_head("pippo")
ll2.insert_at_head("paperino")
ll2.insert_at_head("pluto")

print(ll2.successor("pippo"))
ll2.insert_at_head("clarabella")
print(ll2.predecessor("pippo"))
print(ll2.predecessor("clarabella"))