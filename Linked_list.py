
class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

    def  __str__ (self):
        return ( "Node with value: " + str(self.value) + "\nNext:"+ str(self.next))
    

class LinkedList:
    def __init__ (self):
        self.head=None 
    
    def insert(self,elem):
        current=self.head
        nodo=Node(elem)

        if current is None:
            self.head=nodo 
        else:
            nodo.next=current 
            self.head=nodo 
    
    def print(self):
        current=self.head 
        while current:
            print(current.value, end = ' ')
            current=current.next 

        print(end='\n')
    
    def minimum(self):
        current=self.head
        min=self.head
        while current:
            if current.value < min.value:
                min=current
            current=current.next 

        return min.value 
    
    def maximum(self):
        current=self.head
        max=self.head
        while current:
            if current.value > max.value:
                max=current
            current=current.next 

        return max.value 


    
g=LinkedList()
g.insert(4)
g.insert(5)
g.insert(6)
g.insert(2)

g.print()
print(g.minimum())
print(g.maximum())
    
# lista = [1,5,8,9,3]
# ll = LinkedList(lista)
# print(ll.minimum())
# print(ll.maximum())