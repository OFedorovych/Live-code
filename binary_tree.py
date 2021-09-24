class Tree:

    def __init__(self):
        self.root = None

    def search(self, value):
        found_node = self._search(self.root, value)
        if found_node is None:
            return False
        else:
            return True

    def delete(self, value):
        pass

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        
        self._insert(self.root, value)
    
    def max_value(self):
        pass

    def min_value(self):
        pass

    def _insert(self, current_node, value):
        #go to right
        if value > current_node.value:
            #add right leaf if absent
            if current_node.right is None:
                current_node.right = Node(value, current_node)
                return
            #search for a proper position in right branch
            return self._insert(current_node.right, value)
            
        else:
            #add left leaf if absent
            if current_node.left is None:
                current_node.left = Node(value, current_node)
                return
            return self._insert(current_node.left, value)

    def _search(self, noda_to_check, value):

        #no more nodes, our parent is a leaf
        #we found: searched  value is equal to the node
        if ((noda_to_check == None) or (noda_to_check.value == value)):
            return noda_to_check
        
        if value > noda_to_check.value:
            # go right
            return self._search(noda_to_check.right, value)
        else:
            # go left
            return self._search(noda_to_check.left, value)

class Node:

    def __init__(self, value, parent = None):
        self.right = None
        self.left = None
        self.parent = None
        self.value = value


tree = Tree()
tree.insert(15)
tree.insert(6)
tree.insert(7)
tree.insert(4)
tree.insert(5)
tree.insert(23)
tree.insert(71)
tree.insert(50)


print(tree.search(15))
print(tree.search(6))
print(tree.search(7))
print(tree.search(5))

