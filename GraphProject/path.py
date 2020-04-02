from roottree import RootTree
from collections import defaultdict
import heapq

def dfs(g, startVertex):
    queue = [startVertex]
    visited = set()
    visited.add(startVertex)
    tree = RootTree(startVertex)
    listaOutput = [startVertex]
    while len(queue) > 0:
            currentVertex = queue.pop()
            for nextVertex in g.outBound(currentVertex):
                if nextVertex not in visited:
                    queue.append(nextVertex)
                    visited.add(nextVertex)
                    tree.addChild(currentVertex, nextVertex)
                    listaOutput.append(nextVertex)
    return listaOutput


def dfsForTree(g, startVertex):
    queue = [startVertex]
    visited = set()
    visited.add(startVertex)
    tree = RootTree(startVertex)
    listaOutput = [startVertex]
    while len(queue) > 0:
            currentVertex = queue.pop()
            for nextVertex in g.outBound(currentVertex):
                if nextVertex not in visited:
                    queue.append(nextVertex)
                    visited.add(nextVertex)
                    tree.addChild(currentVertex, nextVertex)
                    listaOutput.append(nextVertex)
    return tree


def prim(graph, cost, starting_vertex):
    totalCost = 0
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = []
    for to in graph.parse_outbound(starting_vertex):
        edges.append((cost[(starting_vertex, to)], starting_vertex, to))

    heapq.heapify(edges)

    while edges:
        edge_cost, vertex, to = heapq.heappop(edges)

        if to not in visited:
            visited.add(to)
            mst[vertex].add(to)
            totalCost += cost[(vertex, to)]

            for to_next in graph.parse_outbound(to):
                if to_next not in visited:
                    edges.append((cost[(to, to_next)], to, to_next))
                    heapq.heapify(edges)

                    heapq.heappush(edges, edges[0])
                    break

    return mst, totalCost


def hamiltonian(graph, cost, startVertex, path, visited, totalCost, const_vertex):
    if len(path) == graph.vertices:
        print(totalCost)

    while len(path) < graph.vertices:
        for nextVertex in graph.outBound(startVertex):
            if nextVertex not in visited:
                visited.add(nextVertex)
                path.append(nextVertex)
                totalCost += cost[(startVertex, nextVertex)]
                hamiltonian(graph, cost, nextVertex, path, visited, totalCost, const_vertex)

    if const_vertex in graph.outBound(path[graph.vertices - 1]):
        return path
    else:
        return "Hamilton cycle not found"


def dijkstra(g, cost, targetVertex):
    '''
    Returns the tree of the minimum cost walks from startVertex
    '''
    try:
        queue = []
        tree = RootTree(targetVertex)
        minCosts = {targetVertex: 0}
        heapq.heappush(queue, (0, targetVertex, None))
        currCost = 0
        while queue != []:
            currCost, currVertex, parent = heapq.heappop(queue)
            if currCost > minCosts[currVertex]:
                continue
            if parent is not None:
                tree.addChild(parent, currVertex)

            children = g.parse_inbound(currVertex)
            for vertex in children:
                if not vertex in minCosts.keys() or \
                        currCost + cost[(vertex, currVertex)] < minCosts[vertex]:
                    minCosts[vertex] = currCost + cost[(vertex, currVertex)]
                    heapq.heappush(queue, (minCosts[vertex], vertex, currVertex))

        return tree
    except IOError:
        raise ValueError("Something went wrong.")


def getPath(tree, targetVertex):
    ''' Returns the list of vertices from the root of a tree to the `targetVertex`
        Returns None if the targetVertex is not in the tree
    '''
    try:
        if not tree.isVertex(targetVertex):
            raise ValueError("Path does not exist!")

        path = []
        currVertex = targetVertex
        while currVertex != None:
            path.append(currVertex)
            parent = tree.getParent(currVertex)
            currVertex = parent

        path.reverse()
        return path

    except Exception as e:
        print(e)


def computeCost(path, costs):
    try:
        if path == None:
            raise ValueError("So, the cost can't be computed...")

        path.reverse()
        if path is None:
            return None
        totalCost = 0
        for vertexInd in range(len(path) - 1):
            totalCost += costs[(path[vertexInd], path[vertexInd + 1])]
        return totalCost

    except Exception as e:
        print(e)

