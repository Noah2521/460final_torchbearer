import heapq

def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    #Priority queue of Dijkstra's and graph key
    prioQueue = []
    fuelCosts = {node : float('inf') for node in graph}

    #Set source distance to 0 and push into prio queue
    fuelCosts[source] = 0 
    heapq.heappush(prioQueue,(0, source))

    #Dijkstra's
    while prioQueue:

        #Pop the current node
        dist, curr = heapq.heappop(prioQueue)

        #If the current edge weight is greater than the node's key value, skip th search
        if dist > fuelCosts[curr]:
            continue
        
        #For every edge for each node, if the total path weight is less than the recorded weight, set the new cost for the path 
        #and add the path to the priority queue.
        for edge, weight in graph[curr]:
            if fuelCosts[curr] + weight < fuelCosts[edge]:
                fuelCosts[edge] = fuelCosts[curr] + weight
                heapq.heappush(prioQueue, (fuelCosts[edge], edge))

    return fuelCosts

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    #Create list and add spawn element
    sourceList = []
    sourceList.append(spawn)

    #Fill list full of relics, ignore duplicate nodes
    for relic in relics:
        if relic in sourceList:
            continue
        sourceList.append(relic)

    #Add ending node and return list of sources
    sourceList.append(exit_node)

    return sourceList

def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    totalFuelCost = {}
    sourceList = select_sources(spawn,relics,exit_node)

    for node in sourceList:
        totalFuelCost[node] = run_dijkstra(graph, node)

    return totalFuelCost



def main():
    graph = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    relics = ['B', 'C', 'D']
    print(precompute_distances(graph, 'S', relics, 'T'))

main()