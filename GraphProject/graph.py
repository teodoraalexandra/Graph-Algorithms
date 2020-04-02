class Graph:
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)] \
                      for row in range(vertices)]
        self.V = vertices

        self.__n = vertices
        self.__inbound = {}
        self.__outbound = {}

        for vertex in range(0, self.__n):
            self.__inbound[vertex] = []
            self.__outbound[vertex] = []

        self.dcosts = {
            "origin": [],
            "target": [],
            "edge": []
        }
        self.din = {}
        self.dout = {}
        self.vertices = 0
        self.edges = 0

        self.read_graph()

    def read_graph(self):
        f = open('lab5.txt', "r")

        line = f.readline().strip()
        tok = line.split(" ")
        self.vertices = int(tok[0])
        self.edges = int(tok[1])
        line = f.readline().strip()
        while line != "":
            tok = line.split(" ")
            self.dcosts["origin"].append(tok[0])  # origin
            self.dcosts["target"].append(tok[1])  # target
            self.dcosts["edge"].append(tok[2])  # cost of edge
            line = f.readline().strip()

        self.generateGraph(self.dcosts, self.vertices, self.edges)
        f.close()

    def generateGraph(self, dcosts, vertices, edges):
        for i in range(vertices):
            self.din[i] = []
            self.dout[i] = []

        for i in range(edges):
            origin = int(dcosts['origin'][i])
            target = int(dcosts['target'][i])
            self.dout[origin].append(target)

        for i in range(edges):
            origin = int(dcosts['origin'][i])
            target = int(dcosts['target'][i])
            self.din[target].append(origin)

    def add_edge(self, x, y):
        # connect two vertices x and y by an edge, from x to y
        # x and y must be existing vertices
        # returns True if the edge was added, False if the edge already exists
        if self.is_edge(x, y):
            return False
        self.__inbound[y].append(x)
        self.__outbound[x].append(y)
        return True

    def is_edge(self, x, y):
        # check whether or not there exists an edge from x to y
        # x and y must be existing vertices
        # this function will return either True or False
        return y in self.__outbound[x]

    def parse_outbound(self, x):
        # this function returns an enumerable containing all the outbound
        # neighbours of x.
        # x must be an existing vertex
        return self.__outbound[x]

    def parse_inbound(self, x):
        return self.__inbound[x]

    def outBound(self, vertex):
        if vertex in self.dout.keys():
            return self.dout[vertex]
        else:
            return "This vertex does not exist."

    def isSafe(self, v, pos, path):
        # Check if current vertex and last vertex in path are adjacent
        if self.graph[path[pos - 1]][v] == 0:
            return False

        # Check if current vertex not already in path
        for vertex in path:
            if vertex == v:
                return False

        return True

    def hamCycleUtil(self, path, pos):
        # base case: if all vertices are included in the path
        if pos == self.V:
            # Last vertex must be adjacent to the first vertex in path to make a cycle
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        # Try different vertices as a next candidate
        # in Hamiltonian Cycle. We don't try for 0 as
        # we included 0 as starting point in in hamCycle()
        for v in range(1, self.V):
            if self.isSafe(v, pos, path) == True:
                path[pos] = v

                if self.hamCycleUtil(path, pos + 1) == True:
                    return True

                # Remove current vertex if it doesn't lead to a solution
                path[pos] = -1

        return False

    def hamCycle(self):
        path = [-1] * self.V

        ''' Let us put vertex 0 as the first vertex  
            in the path. If there is a Hamiltonian Cycle,  
            then the path can be started from any point 
            of the cycle as the graph is undirected '''
        path[0] = 0

        if self.hamCycleUtil(path, 1) == False:
            print("Solution does not exist\n")
            return False

        self.printSolution(path)
        return True

    def printSolution(self, path):
        print("Solution Exists! Hamiltonian Cycle is the following: ")
        for vertex in path:
            print(vertex, end="")
        print(path[0])  #this line if for hamiltonian cycle (without it, it would be just hamiltonian path
        print("\n")


def createDemoGraph():
    f = open('not_ham.txt', "r")

    line = f.readline().strip()
    tok = line.split(" ")
    graph = Graph(int(tok[0]))
    line = f.readline().strip()
    dcost = {}
    while line != "":
        tok = line.split(" ")
        edge = (int(tok[0]), int(tok[1]))
        graph.add_edge(int(tok[0]), int(tok[1]))
        dcost.update({edge: int(tok[2])})
        line = f.readline().strip()

    f.close()
    return graph, dcost

