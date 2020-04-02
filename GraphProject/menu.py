from graphController import GraphController
from graph import Graph
from graph import *
from path import *
import random


class UI:
    def __init__(self, controller):
        self.controller = controller

    def _printMessage(self):
        print("The graph is automatically generated from the file graph.txt")
        self._printMenu()

    def _printMenu(self):
        print("Main menu: ")
        print("\t1. Get the number of vertices")
        print("\t2. Print all vertices")
        print("\t3. Find if an edge exists between two vertices")
        print("\t4. In degree of a vertex")
        print("\t5. Out degree of a vertex")
        print("\t6. Set of inbound edges of a vertex")
        print("\t7. Set of outbound edges of a vertex")
        print("\t8. Update the cost of an edge")
        print("\t9. Print graph")
        print("\t10. Find isolated vertices")
        print("\t11. Modify the graph")
        print("\t12. Copy graph")
        print("\t13. Print ALL subgraphs")
        print("\t14. Print UNIQUE subgraphs")
        print("\t15. Print UNIQUE subgraphs - ONLY LISTS")
        print("\t16. Print ALL subgraphs - ONLY LISTS")
        print("\t17. Find the lowest cost walk between two given vertices")
        print("\t18. Minimal spanning tree using Prim Algorithm")
        print("\t19. Find the Hamiltonian cycle")
        print("\t0. Exit the program")

        i = int(input(": "))

        if i == 1:
            print(controller.getTheNumberOfVertices())

            self._printMenu()

        elif i == 2:
            print(controller.parseVertices())

            self._printMenu()

        elif i == 3:
            vertex1 = input("Enter vertex number 1: ")
            vertex2 = input("Enter vertex number 2: ")
            try:
                if vertex1.isnumeric() == False or vertex2.isnumeric() == False:
                    raise ValueError("Enter integers!")

                vertex1 = int(vertex1)
                vertex2 = int(vertex2)
                if vertex1 in controller.parseVertices() and vertex2 in controller.parseVertices():
                    if controller.findIfEdge(vertex1, vertex2):
                        print("This edge exists")
                    else:
                        print("This edge does NOT exist")
                else:
                    print("One of the vertices does not exist")

                self._printMenu()

            except ValueError as i:
                print(i)

        elif i == 4:
            vertex = input("Enter the vertex for in degree: ")
            try:
                if vertex.isnumeric() == False:
                    raise ValueError("Enter integer!")

                vertex = int(vertex)
                print(controller.inDegree(vertex))
            except ValueError as i:
                print(i)

            self._printMenu()

        elif i == 5:
            vertex = input("Enter the vertex for out degree: ")
            try:
                if vertex.isnumeric() == False:
                    raise ValueError("Enter integer!")

                vertex = int(vertex)
                print(controller.outDegree(vertex))
            except ValueError as i:
                print(i)

            self._printMenu()

        elif i == 6:
            vertex = input("Enter the vertex for d-in: ")
            try:
                if vertex.isnumeric() == False:
                    raise ValueError("Enter integer!")

                vertex = int(vertex)
                print(controller.inBound(vertex))
            except ValueError as i:
                print(i)

            self._printMenu()

        elif i == 7:
            vertex = input("Enter the vertex for d-out: ")
            try:
                if vertex.isnumeric() == False:
                    raise ValueError("Enter integer!")

                vertex = int(vertex)
                print(controller.outBound(vertex))
            except ValueError as i:
                print(i)

            self._printMenu()

        elif i == 8:
            origin = input("Enter the origin: ")
            target = input("Enter the target: ")
            try:
                if origin.isnumeric() == False or target.isnumeric() == False:
                    raise ValueError("Enter integers!")

                if controller.findIfEdge(origin, target):
                    print("There is no edge between these two vertices")
                else:
                    edge = input("Enter the cost of the edge: ")
                    controller.updateCost(origin, target, edge)
                    print("The cost has been updated")
                    # print("There is no edge between these two vertices")
            except ValueError as i:
                print(i)

            self._printMenu()

        elif i == 9:
            controller.printGraph()

            self._printMenu()

        elif i == 10:
            print(controller.findIsolatedVertices())

            self._printMenu()

        elif i == 11:
            self._printMenuToModify()

        elif i == 12:
            controller.copyGraph()
            print("The graph has been copied to copy.txt")

            self._printMenu()

        elif i == 13:
            self._printAll()

            self._printMenu()

        elif i == 14:
            self._printUnique()

            self._printMenu()

        elif i == 15:
            self._printLists()

            self._printMenu()

        elif i == 16:
            self._printListsAll()

            self._printMenu()

        elif i == 17:
            self._dijkstraAlg()

            self._printMenu()

        elif i == 18:
            self._primAlg()

            self._printMenu()

        elif i == 19:
            self._hamiltonian()

            self._printMenu()

        elif i == 0:
            return
        else:
            print("Invalid command! \n")
            self._printMenu()

    def _hamiltonian(self):
        lista_mare = []
        for i in range(g.vertices):
            lista_mica = []
            for j in range(g.vertices):
                if g.is_edge(i, j):
                    lista_mica.append(1)
                else:
                    lista_mica.append(0)
            lista_mare.append(lista_mica)

        new_graph = Graph(g.vertices)
        new_graph.graph = lista_mare
        new_graph.hamCycle()

    def _primAlg(self):
        print("\nStarting Prim Algorithm...")
        r = list((controller.parseVertices()))

        max = 0
        for i in r:
            minimum_spanning_tree, max_cost = prim(g, cost, i)
            print(dict(minimum_spanning_tree), "\n")
            if max_cost > max:
                max = max_cost
        print("Total cost of mst: ", max, "\n")

    def _dijkstraAlg(self):
        startVertex = int(input("Enter the start vertex: "))
        targetVertex = int(input("Enter the target vertex: "))
        print("Printing the tree...")
        tree = dijkstra(g, cost, targetVertex)
        tree.printTree()

        bestPath = getPath(tree, startVertex)
        if bestPath != None:
            print("Best path: ", bestPath)

        minimumCost = computeCost(bestPath, cost)
        if minimumCost != None:
            print("The lowest cost: ", minimumCost)

    def _printAll(self):
        vertices = controller.getTheNumberOfVertices()
        graph = Graph(vertices)
        for i in controller.parseVertices():
            treeForPrint = dfsForTree(graph, i)
            print("The tree with startVertex: ", i)
            print(treeForPrint)
            print("\n")

    def _printListsAll(self):
        vertices = controller.getTheNumberOfVertices()
        graph = Graph(vertices)
        for i in controller.parseVertices():
            tree = dfs(graph, i)
            print("The tree with startVertex: ", i)
            print(tree)
            print("\n")

    def _printUnique(self):
        vertices = controller.getTheNumberOfVertices()
        graph = Graph(vertices)
        firstTree = dfs(graph, 0)

        for i in controller.parseVertices():
            tree = dfs(graph, i)
            treeForPrint = dfsForTree(graph, i)
            if sorted(firstTree) == sorted(tree):
                firstTree = tree
            else:
                print("The tree with startVertex: ", i)
                print(treeForPrint)
                print("\n")
            firstTree = tree

    def _printLists(self):
        vertices = controller.getTheNumberOfVertices()
        graph = Graph(vertices)
        firstTree = dfs(graph, 0)

        for i in controller.parseVertices():
            tree = dfs(graph, i)
            if sorted(firstTree) == sorted(tree):
                firstTree = tree
            else:
                print("The tree with startVertex: ", i)
                print(tree)
                print("\n")
            firstTree = tree

    def _printMenuToModify(self):
        print("Modify the graph: ")
        print("\t1. Add edge")
        print("\t2. Remove edge")
        print("\t3. Add vertex")
        print("\t4. Remove vertex")
        print("\t5. Back to main menu")

        i = input(": ")
        if i == "1":
            origin = input("Enter the origin: ")
            target = input("Enter the target: ")
            edge = input("Enter the cost of the edge: ")

            try:
                if origin.isnumeric() == False or target.isnumeric() == False:
                    raise ValueError("Enter integers!")
                origin = int(origin)
                target = int(target)
                if origin in self.controller.parseVertices() and target in self.controller.parseVertices():
                    if self.controller.findIfEdge(origin, target):
                        print("This edge exists")
                    else:
                        controller.addEdge(origin, target, edge)
                else:
                    print("One of the vertices does not exist")

                self._printMenu()
            except ValueError as i:
                print(i)

        elif i == "2":
            origin = input("Enter the origin: ")
            target = input("Enter the target: ")
            edge = input("Enter the cost of the edge: ")

            try:
                if origin.isnumeric() == False or target.isnumeric() == False:
                    raise ValueError("Enter integers!")
                origin = int(origin)
                target = int(target)
                if origin in self.controller.parseVertices() and target in self.controller.parseVertices():
                    if self.controller.findIfEdge(origin, target):
                        controller.removeEdge(origin, target, edge)
                    else:
                        print("This edge does NOT exist")
                else:
                    print("One of the vertices does not exist")
                self._printMenu()
            except ValueError as i:
                print(i)

        elif i == "3":
            vertex = input("Enter the vertex you want to add: ")
            try:
                if vertex.isnumeric() == False:
                    raise ValueError("Enter integer!")

                vertex = int(vertex)
                if vertex in controller.parseVertices():
                    print("This vertex already exist")
                else:
                    controller.addVertex(vertex)

                self._printMenu()
            except ValueError as i:
                print(i)

        elif i == "4":
            vertex = input("Enter the vertex you want to remove: ")
            try:
                if vertex.isnumeric() == False:
                    raise ValueError("Enter integer!")
                vertex = int(vertex)
                if vertex in controller.parseVertices():
                    controller.removeVertex(vertex)
                else:
                    print("This vertex does NOT exists")

                self._printMenu()
            except ValueError as i:
                print(i)

        elif i == "5":
            self._printMenu()

        else:
            print("Invalid command! \n")
            self._printMenuToModify()


g, cost = createDemoGraph()
controller = GraphController(g)
ui = UI(controller)
ui._printMessage()
