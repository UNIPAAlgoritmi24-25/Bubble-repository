from typing import Self

# TODO facci una enum
RED = "RED"
BLACK = "BLACK"


class Node:
    def __init__(
        self,
        key: int | float | str,
        color: str = RED,
        left: Self | None = None,
        right: Self | None = None,
        parent: Self | None = None,
    ) -> None:
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self) -> str:
        return f"{self.key}:{'R' if self.color == RED else 'B'}"


class RedBlackTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    # ------------------------------------------------------------------
    # Rotations (left / right)
    # ------------------------------------------------------------------
    def _left_rotate(self, x: Node) -> None:
        y = x.right
        assert y is not None, "Cannot left-rotate when right child is None"

        # Perform rotation
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _right_rotate(self, x: Node) -> None:
        y = x.left
        assert y is not None, "Cannot right-rotate when left child is None"

        x.left = y.right
        if y.right is not None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    # ------------------------------------------------------------------
    # transplant
    # ------------------------------------------------------------------
    def _transplant(self, u: Node, v: Node | None) -> None:
        if u.parent is None:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    # ------------------------------------------------------------------
    # Search, max, min, predecessor, successor
    # ------------------------------------------------------------------
    def search(self, key: int | float | str) -> Node | None:
        cur = self.root
        while cur is not None and cur.key != key:
            cur = cur.left if key < cur.key else cur.right
        return cur

    def minimum(self, node: Node | None = None) -> Node | None:
        node = self.root if node is None else node
        while node is not None and node.left is not None:
            node = node.left
        return node

    def maximum(self, node: Node | None = None) -> Node | None:
        node = self.root if node is None else node
        while node is not None and node.right is not None:
            node = node.right
        return node

    def predecessor(self, x: Node) -> Node | None:
        if x.left is not None:
            return self.maximum(x.left)
        y = x.parent
        while y is not None and x is y.left:
            x = y
            y = y.parent
        return y

    def successor(self, x: Node) -> Node | None:
        if x.right is not None:
            return self.minimum(x.right)
        y = x.parent
        while y is not None and x is y.right:
            x = y
            y = y.parent
        return y

    # ------------------------------------------------------------------
    # Insert
    # ------------------------------------------------------------------
    def insert(self, key: int | float | str) -> None:
        z = Node(key, color=RED)
        y: Node | None = None
        x = self.root
        while x is not None:
            y = x
            x = x.left if z.key < x.key else x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self._insert_fix(z)

    def _insert_fix(self, z: Node) -> None:
        while z.parent is not None and z.parent.color == RED:
            if z.parent is z.parent.parent.left:
                y = z.parent.parent.right
                if y is not None and y.color == RED:  # due figli rossi
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z is z.parent.right:  # Case 2
                        z = z.parent
                        self._left_rotate(z)
                    # Case 3
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._right_rotate(z.parent.parent)
            else:  # stessa cosa di sopraa ma invertito
                y = z.parent.parent.left
                if y is not None and y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._left_rotate(z.parent.parent)
        self.root.color = BLACK

    # ------------------------------------------------------------------
    # Delete
    # ------------------------------------------------------------------
    def delete(self, key: int | float | str) -> None:
        z = self.search(key)
        if z is None:
            return  # Key not present

        y = z
        y_original_color = y.color

        if z.left is None:
            x = z.right
            self._transplant(z, z.right)
            parent = z.parent
        elif z.right is None:
            x = z.left
            self._transplant(z, z.left)
            parent = z.parent
        else:
            y = self.minimum(z.right)
            assert y is not None
            y_original_color = y.color
            x = y.right
            if y.parent is z:
                parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                if y.right is not None:
                    y.right.parent = y
                parent = y.parent
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == BLACK:
            self._delete_fix(x, parent)

    def _delete_fix(self, x: Node | None, parent: Node | None) -> None:
        """Restore Red-Black properties after deletion."""

        def color(n: Node | None) -> str: 
            return BLACK if n is None else n.color

        while x is not self.root and color(x) == BLACK:
            if parent is None:
                break
            if x is parent.left:
                w = parent.right
                if color(w) == RED:  # Case 1
                    w.color = BLACK
                    parent.color = RED
                    self._left_rotate(parent)
                    w = parent.right
                if color(w.left) == BLACK and color(w.right) == BLACK:  # Case 2
                    w.color = RED
                    x, parent = parent, parent.parent
                else:
                    if color(w.right) == BLACK:  # Case 3
                        if w.left is not None:
                            w.left.color = BLACK
                        w.color = RED
                        self._right_rotate(w)
                        w = parent.right
                    # Case 4
                    w.color = parent.color
                    parent.color = BLACK
                    if w.right is not None:
                        w.right.color = BLACK
                    self._left_rotate(parent)
                    x = self.root
            else:  # mirror image
                w = parent.left
                if color(w) == RED:
                    w.color = BLACK
                    parent.color = RED
                    self._right_rotate(parent)
                    w = parent.left
                if color(w.left) == BLACK and color(w.right) == BLACK:
                    w.color = RED
                    x, parent = parent, parent.parent
                else:
                    if color(w.left) == BLACK:
                        if w.right is not None:
                            w.right.color = BLACK
                        w.color = RED
                        self._left_rotate(w)
                        w = parent.left
                    w.color = parent.color
                    parent.color = BLACK
                    if w.left is not None:
                        w.left.color = BLACK
                    self._right_rotate(parent)
                    x = self.root
        if x is not None:
            x.color = BLACK

    # ------------------------------------------------------------------
    # String representation
    # ------------------------------------------------------------------
    def __str__(self) -> str:
        if self.root is None:
            return "<empty tree>"
        lines: list[str] = []
        queue: list[tuple[Node, int]] = [(self.root, 0)]
        current_level = 0
        level_nodes: list[str] = []
        while queue:
            node, lvl = queue.pop(0)
            if lvl != current_level:
                lines.append(" ".join(level_nodes))
                level_nodes = []
                current_level = lvl
            level_nodes.append(str(node))
            if node.left is not None:
                queue.append((node.left, lvl + 1))
            if node.right is not None:
                queue.append((node.right, lvl + 1))
        if level_nodes:
            lines.append(" ".join(level_nodes))
        return "\n".join(lines)


# ----------------------------- prova ----------------------------------
if __name__ == "__main__":
    t = RedBlackTree()
    for k in [20, 15, 25, 10, 5, 1, 30, 40, 50]:
        t.insert(k)
    print("Tree after insertions:\n", t, sep="")
    t.delete(15)
    t.delete(25)
    print("\nTree after deletions:\n", t, sep="")
