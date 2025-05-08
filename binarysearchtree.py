import random

class Nodo:
    def __init__(self,val):
        self.val=val
        self.parent=None
        self.left=None
        self.right=None

    def add(self,nodo):
        if nodo.val < self.val:
            if self.left:
                self.left.add(nodo)
            else:
                self.left=nodo
                self.left.parent=self
        else:
            if self.right:
                self.right.add(nodo)
            else:
                self.right=nodo
                self.right.parent=self

    def print(self, level=0):
        print(' '*level,self.val)
        if self.left:
            self.left.print(level+1)
        if self.right:
            self.right.print(level+1)

    def minimum(self):
        if self.left:
            self.left.minimum()
        else:
            return self
    def maximum(self):
        if self.right:
            self.right.maximum()
        else:
            return self

    def search(self,x):
        if x > self.val:
            if self.right:
                return self.right.search(x)

        elif x < self.val:
            if self.left:
                return self.left.search(x)

        else:
            current=self.parent
            return self

    def transplant(self,u,v):
        if u.parent == None:
            self= v
            print('parent none')
        elif u == u.parent.left:
            u.parent.left = v
            print('parent sinistro')
        else:
            u.parent.right = v
        if v != None:
            v.parent=u.parent


    def delete(self,v):
        z=self.search(v)
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y=z.right.minimum()
         
            if y.parent != z:
                self.transplant(y,y.right)
                y.right = z.right
                y.right.parent=y
            
            self.transplant(z,y)
            y.left=z.left
           
            y.left.parent=y

 
         
   
           
            


class binarysearchtree:
    def __init__(self):
        self.root=None

    def insert(self, x):
        nodo=Nodo(x)
        if self.root is None:
            self.root=nodo
        else:
            self.root.add(nodo)
    def print(self):
        self.root.print()
    def min(self):
        self.root.minimum()
    def max(self):
        self.root.maximum()
    def search(self,x):
        return self.root.search(x)
    def height(self):
   
        self.root.calculate_height()
    def delete(self,x):
        self.root.delete(x)



j=binarysearchtree()

j.insert(15)
j.insert(7)
j.insert(18)
j.insert(5)
j.insert(14)
j.insert(21)
j.insert(17)
j.print()
#j.min()
#j.max()
#print(j.search(7))
#j.height()
print('\n')
j.delete(18)
j.print()
j.insert(23)
j.insert(33)

j.height()

