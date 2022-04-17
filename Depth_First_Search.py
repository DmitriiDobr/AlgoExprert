"""Depth First Search Graph"""

#Solution 1
class Node1:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node1(name))
        return self

    def depthFirstSearch(self, array):

        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

#Solution 2
class Node2:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node2(name))
        return self

    def depthFirstSearch(self, array):
        if not self.name in array:
            array.append(self.name)
            self.depthFirstSearch(array)
        else:
            for child in self.children:
                if child.children == []:
                    array.append(child.name)
                elif child.children != []:
                    self.children = child.children
                    self.name = child.name
                    array.append(child.name)
                    self.depthFirstSearch(array)
        return array



