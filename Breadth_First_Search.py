"""
Breadth First Search Graph
"""
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        array.append(self.name)
        all_children = self.children
        while True:
            if all_children == []:
                break
            child = all_children.pop(0)
            array.append(child.name)
            all_children += child.children
        return array


