class RootTree:
    def __init__(self, root):
        '''
        Creates a tree with only a root
        '''
        self.root = root
        self.parent = {root: None}
        self.children = {root: []}

    def addChild(self, parent, child):
        '''
        Add a child for the given parent
        Pre: Parent is an existing vertex
             Child doesn't exist in the tree
        '''
        self.parent[child] = parent
        self.children[parent].append(child)
        self.children[child] = []

    def getRoot(self):
        '''
        Return the root of the tree
        '''
        return self.root

    def isVertex(self, theVertex):
        '''
        Boolean function.
        post: true if theVertex is a vertex of the tree
              false otherwise
        '''
        return theVertex in self.parent.keys()

    def getParent(self, child):
        '''
        Return the parent of the given child
        '''
        return self.parent[child]

    def getChildren(self, parent):
        '''
        Returns a generator that produces the children of the given parent
        '''
        return self.children[parent][:]

    def recursiveToTree(self, subroot, depth):
        s = "%s%s\n" % ("\t" * depth, subroot)
        for child in self.getChildren(subroot):
            s = s + self.recursiveToTree(child, depth + 1)

        return s

    def printSubTree(self, root, spaces):
        print(' ' *spaces, root)
        for child in self.children[root]:
            self.printSubTree(child, spaces + 1)

    def printTree(self):
        self.printSubTree(self.root, 0)

    def __str__(self):
        return self.recursiveToTree(self.root, 0)

