from graph import Graph

class GraphController:
    def __init__(self, repo):
        self.repo = repo

    def addEdge(self, origin, target, edge):
        '''
        PRE-CONDITION:
            -origin must be existent
            -target must not be in the dout[origin] -> the edge is in the repo already
        '''
        self.repo.dcosts["origin"].append(str(origin))  # origin
        self.repo.dcosts["target"].append(str(target))  # target
        self.repo.dcosts["edge"].append(str(edge))  # cost of edge

        self.repo.dout[origin].append(target)
        self.repo.din[target].append(origin)

        self.repo.edges += 1
        #self.saveToFile()

    def removeEdge(self, origin, target, edge):
        '''
        PRE-CONDITION: the origin, the target and the edge must exist
        '''
        for i in self.repo.dcosts["origin"]:
            for j in self.repo.dcosts["target"]:
                for z in self.repo.dcosts["edge"]:
                    if i == str(origin) and j == str(target) and z == str(edge):
                        self.repo.dout[origin].remove(target)
                        self.repo.din[target].remove(origin)

                        self.repo.dcosts["origin"].remove(i)  # origin
                        self.repo.dcosts["target"].remove(j)  # target
                        self.repo.dcosts["edge"].remove(z)  # cost of edge

                        self.repo.edges -= 1
                        #self.saveToFile()

                        return


    def addVertex(self, vertex):
        '''
        PRE-CONDITION: the vertex must not exist in the repo, so it can be added
        '''
        self.repo.vertices += 1
        self.repo.dout[vertex] = []
        self.repo.din[vertex] = []
        #self.saveToFile()

    def removeVertex(self, vertex):
        '''
        PRE-CONDITION: the vertex must exist in the repo, so it can be removed
        '''
        n = self.repo.edges
        i = 0
        while i < n:
            x = self.repo.dcosts["origin"][i]
            y = self.repo.dcosts["target"][i]
            z = self.repo.dcosts["edge"][i]
            if vertex == int(x) or vertex == int(y):
                self.repo.dcosts["origin"].remove(x)
                self.repo.dcosts["target"].remove(y)
                self.repo.dcosts["edge"].remove(z)

                self.repo.edges -= 1
                i = i - 1
                n = n - 1
            else:
                i = i + 1

        self.repo.vertices -= 1
        del self.repo.dout[vertex]
        del self.repo.din[vertex]
        #self.saveToFile()

    def inDegree(self, vertex):
        if vertex in self.repo.din.keys():
            return len(self.repo.din[vertex])
        else:
            return "This vertex does not exist."

    def outDegree(self, vertex):
        if vertex in self.repo.dout.keys():
            return len(self.repo.dout[vertex])
        else:
            return "This vertex does not exist."

    def inBound(self, vertex):
        if vertex in self.repo.din.keys():
            return self.repo.din[vertex]
        else:
            return "This vertex does not exist."

    def outBound(self, vertex):
        if vertex in self.repo.dout.keys():
            return self.repo.dout[vertex]
        else:
            return "This vertex does not exist."

    def findIsolatedVertices(self):
        '''
        We check every vertex -> they are isolated if they have no inbound and no outbound
        '''
        print("The isolated vertices are: ")
        for vertex in self.repo.dout.keys():
            if self.repo.dout[vertex] == [] and self.repo.din[vertex] == []:
                return vertex

    def findIfEdge(self, vertex1, vertex2):
        if vertex1 in self.repo.dout.keys() or vertex2 in self.repo.dout.keys():
            if vertex2 in self.repo.dout[vertex1] or vertex1 in self.repo.dout[vertex2]:
                return True
            else:
                return False

    def parseVertices(self):
        parse = []
        for vertex in self.repo.dout.keys():
            parse.append(vertex)
        return parse

    def updateCost(self, origin, target, edge):
        n = self.repo.edges
        i = 0
        print("Cost before update: ", self.repo.dcosts["edge"][i])
        while i < n:
            x = self.repo.dcosts["origin"][i]
            y = self.repo.dcosts["target"][i]
            if origin == int(x) and target == int(y):
                self.repo.dcosts["edge"][i] = edge
                print("Cost after update: ", self.repo.dcosts["edge"][i])
            i = i + 1


        #self.saveToFile()

    def getTheNumberOfVertices(self):
        return self.repo.vertices

    def getTheNumberOfEdges(self):
        return self.repo.edges

    def printGraph(self):
        f = open('graph.txt', "r")

        line = f.readline().strip()
        tok = line.split(" ")
        vertices = int(tok[0])
        print(vertices, ' ', end="")
        edges = int(tok[1])
        print(edges)
        line = f.readline().strip()
        while line != "":
            tok = line.split(" ")
            print(tok[0], ' ', end="")  # origin
            print(tok[1], ' ', end="")  # target
            print(tok[2], ' ', end="")  # cost of edge

            print("\n")
            line = f.readline().strip()

        f.close()

    def saveToFile(self):
        f = open('graph.txt', "w")
        f.write(str(self.repo.vertices))
        f.write(" ")
        f.write(str(self.repo.edges))
        f.write("\n")
        for j in range(self.repo.edges):
            for i in self.repo.dcosts:
                f.write(self.repo.dcosts[i][j])
                f.write(" ")
            f.write("\n")
        f.close()

    def copyGraph(self):
        f = open('copy.txt', "w")
        f.write(str(self.repo.vertices))
        f.write(" ")
        f.write(str(self.repo.edges))
        f.write("\n")
        for j in range(self.repo.edges):
            for i in self.repo.dcosts:
                f.write(self.repo.dcosts[i][j])
                f.write(" ")
            f.write("\n")
        f.close()
