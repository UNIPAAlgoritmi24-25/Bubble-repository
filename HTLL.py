
import random
from sympy import nextprime


"""Avrebbe senso importare il file delle LinkedList ma la sezione precedentemente definita non prevede il metodo delete.
Pertanto riporto di seguito il codice che lo comprende """

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
        return succ.value if succ else None
    


    def predecessor(self, value):
        aus = self.head
        prec = None
        while aus:
            if aus.value < value:
                if prec is None or aus.value > prec.value:
                    prec = aus
            aus = aus.next
        return prec.value if prec else None
    
    
    
    def search(self, value):
        aus = self.head
        while aus:
            if aus.value == value:
                return aus
            aus = aus.next
        return None  
    

    def delete(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        aus = self.head
        current = self.head.next
        while current:
            if current.value == value:
                aus.next = current.next
                return
            aus = current
            current = current.next




class HashTableLl:
    def __init__(self, size=10):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]
        self.p = nextprime(size)    #moltiplicare size per un fattore da decidere
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)


    def hash_function(self, key):
        if not isinstance(key, int):
            raise ValueError("Only int keys allowed")
        return ((self.a * key + self.b) % self.p) % self.size


    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].insert_at_head(key)


    def search(self, key):
        index = self.hash_function(key)
        return self.table[index].search(key)


    def delete(self, key):
        index = self.hash_function(key)
        self.table[index].delete(key)


    def __str__(self):
        result = ""
        for i, linked_list in enumerate(self.table):
            result += str(i) + ":"+ str(linked_list)+ "\n"
        return result
    

def carica_da_file(nome_file):
    
    A=LinkedList()
    with open(nome_file, 'r') as file:
        contenuto = file.read()
        valori = contenuto.split(',')
        
        print("Valori caricati dal file:")
        
        # Itera su ogni valore nella lista
        for valore in valori:
            A.insert_at_head(valore)
    return A
            
