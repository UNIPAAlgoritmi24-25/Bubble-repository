class Nodo:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Nodo(val)
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while current:
            if val < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    new_node.parent = current
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    new_node.parent = current
                    return

    def _print(self, node, level=0):
        if node:
            print('  ' * level, node.val)
            self._print(node.left, level + 1)
            self._print(node.right, level + 1)

    def print(self):
        self._print(self.root)

    def minimum(self, node=None):
        if node is None:
            node = self.root
        while node.left:
            node = node.left
        return node

    def maximum(self, node=None):
        if node is None:
            node = self.root
        while node.right:
            node = node.right
        return node

    def search(self, val):
        current = self.root
        while current:
            if val == current.val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return None

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def delete(self, val):
        node = self.search(val)
        if not node:
            return
        if not node.left:
            self.transplant(node, node.right)
        elif not node.right:
            self.transplant(node, node.left)
        else:
            successor = self.minimum(node.right)
            if successor.parent != node:
                self.transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self.transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    def predecessor(self, val):
        predecessor = None
        current = self.root
        
        while current:
            if val > current.val:
                predecessor = current 
                current = current.right
            else:
                current = current.left
        
        return predecessor
    
    def successor(self, val):
        successor = None
        current = self.root
        
        while current:
            if val < current.val:
                successor = current 
                current = current.left
            else:
                current = current.right
        
        return successor

def carica_da_file(nome_file):
    bst = BinarySearchTree()
    with open(nome_file, 'r') as file:
        contenuto = file.read()
        valori = contenuto.replace('\n', ',').split(',')
        
        for valore in valori:
            valore = valore.strip()
            if valore:
                try:
                    if '.' in valore:
                        bst.insert(float(valore))
                    else:
                        bst.insert(int(valore))
                except ValueError:
                    pass  
    return bst
