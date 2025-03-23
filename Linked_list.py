
class LinkedListNode:
    def __init__ (self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    #def  __str__ (self):
        #return ( "Node with value: " + str(self.value) + "\nNext:"+ str(self.next))
    



class LinkedList:
    def __init__ (self,values_list =[]):
        self.values_list = values_list
        self.linked_list = []
        #self.L.head = None
        #attenzione indexerror
        #gestire casi specifici
        for n in range(len(self.values_list)):
            if n == 0 and len(self.values_list) > 1:
                self.L_head = LinkedListNode(self.values_list[0],self.values_list[1])
                self.linked_list.append(self.L_head)
            if n> 0 and n < (len(self.values_list) -1):
                self.node = LinkedListNode(self.values_list[n],self.values_list[n+1])
                self.linked_list.append (self.node)
            if n == (len (self.values_list)-1):   
                self.L_tail = LinkedListNode(self.values_list[-1], None)
                self.linked_list.append (self.L_tail)

    
    def __str__ (self):
        pass
    
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
    
# lista = [1,5,8,9,3]
# ll = LinkedList(lista)
# print(ll.minimum())
# print(ll.maximum())