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

    #Dijkstra's Algorithm
    while prioQueue:

        #Pop the current node
        dist, curr = heapq.heappop(prioQueue)

        #If the current edge weight is greater than the node's key value, skip the search
        if dist > fuelCosts[curr]:
            continue
        
        #For every edge for each node, if the total path weight is less than the recorded weight, set the new cost for the path 
        #and add the node with its updated fuel cost the priority queue.
        for edge, weight in graph[curr]:
            if fuelCosts[curr] + weight < fuelCosts[edge]:
                fuelCosts[edge] = fuelCosts[curr] + weight
                heapq.heappush(prioQueue, (fuelCosts[edge], edge))

    return fuelCosts

#Combine all the methods to precompute the distances for all nodes. 
#Took me a bit longer than it should have to figure out.
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
    #Nested adjacency list with fuel costs and source nodes. Creates list of sources.
    allFuelCosts = {}
    sourceList = select_sources(spawn, relics, exit_node)

    #Run dijkstra's on every source node in the source list.
    for node in sourceList:
        allFuelCosts[node] = run_dijkstra(graph, node)

    return allFuelCosts

# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    #Final route containing total fuel cost and order of nodes explored.
    optimalRoute = [float('inf'), []]
    
    #Used to track remaining relics to track.
    orderOfRelicsVisited = []
    relicsRemaning = set(relics)
    currentFuelCost = 0.0

    #Case for an empty relic list.
    if not relics:
        fuelCost = dist_table.get(spawn, {}).get(exit_node, float('inf'))
        #Case for cost from S to T, return cost between two.
        if fuelCost < float('inf'):
            return (fuelCost, []) 
        #No path from S to T exists
        else:
            return (float('inf'), [])

    _explore(dist_table, spawn, relicsRemaning, orderOfRelicsVisited, currentFuelCost, exit_node, optimalRoute)

    #Return the route if it was found, else return and empty tuple.
    if (optimalRoute[0] < float('inf')):
        return (optimalRoute[0], optimalRoute[1])
    else:
        return (float('inf'), [])


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """

    #The pruning case. We stop exploring for the current order if our current path fuel costs is higher than or equal tos the recorded best cost
    #The pruning condition safe because we're working with guaranteed nonnegative, so there's no cycles or edges that could result in lower paths over iterations.
    if cost_so_far >= best[0]:
        return 
    
    #Base case. All relics have been explored.
    if not relics_remaining:
        #If exit node T can be reached and ended at, update fuelcost if path is lower than best 
        totalFuel = cost_so_far + dist_table.get(current_loc, {}).get(exit_node, float('inf'))
        #if current path's fuel cost is better than recorded, write current path into history
        if totalFuel < best[0]:
            best[0] = totalFuel
            best[1] = list(relics_visited_order) 
        return
    
    #Recursive case + actual search. Move through each relic and test every combination through recursion.
    for relic in relics_remaining:
        #Get cost edge between current node and next relic
        fuelCost = dist_table.get(current_loc, {}).get(relic, float('inf'))
        #Unreachable node
        if fuelCost == float('inf'):
            continue

        #Add next relic to explore queue and recurse
        relics_remaining.remove(relic)
        relics_visited_order.append(relic)

        #Explore next node
        _explore(dist_table, relic, relics_remaining, relics_visited_order, cost_so_far + fuelCost, exit_node, best)

        #Backtrack to try next relic order
        relics_remaining.add(relic)
        relics_visited_order.pop()


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    #Pretty simple. Formats the graph into a dictionary and then runs optimal route algorithm to find the min fuel cost and relic order.
    dist_table = precompute_distances(graph, spawn, relics, exit_node)

    return find_optimal_route(dist_table, spawn, relics, exit_node)


def main():
    graph = {
      'S' : [('R1', 1), ('R2', 3)],
      'R1' : [('V', 2), ('T', 2)],
      'R2' : [('R1', 1), ('T', 4)],
      'V' : [('R2', 2)],
      'T' : []
    }

    print(solve(graph, 'S', ['R1','R2'], 'T'))




if __name__ == "__main__":
 main()
