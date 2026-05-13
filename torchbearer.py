"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: ___________________________
Student ID:   ___________________________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """    
    explanation = """
    - **Why a single shortest-path run from S is not enough:** \n
    - SSSP run from S only provides shortest paths to chamber nodes but doesn't provide shortest paths between chambers. \n

    - **What decision remains after all inter-location costs are known:** \n
    - The lowest cost path between two relics is chosen first. \n

    - **Why this requires a search over orders (one sentence):** \n
    - Every order combination provides a different cost, thus every order must be tested to find the minimum.\n""" 

    
    return explanation


# =============================================================================
# PART 2
# =============================================================================

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

        #If the current edge weight is greater than the node's key value, skip th search
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
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    explanation = """
    Part 3a \n
    For nodes already finalized (in S): Nodes in S have found the shortest possible path from the start node to itself. \n 
    For nodes not yet finalized (not in S): Nodes not in S have not found the least cost path and contain the current lowest cost path from the start node.\n
    
    Part 3b \n
    - **Initialization : why the invariant holds before iteration 1:**
    - All nodes are unexplored and contain inf for their values. Inf values for each node is appropriate since no paths have been explored yet. \n

    - **Maintenance : why finalizing the min-dist node is always correct:**
    - Since no negative edge values exist, the possiblity for negative cycles and lower cost paths through multiple iterations is not possible. \n

    - **Termination : what the invariant guarantees when the algorithm ends:**
    - When the algorithm ends, all nodes will be in S and contain the lowest possible cost paths possible from the start node, though the relics nodes, and to the end node. \n

    Part 3c \n
    - By calculating the shortest distances between relic nodes, the start node, and end node, we are able to decide which edge to start with when building the path.
    """
    
    return explanation


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return "TODO"


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
    pass


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
    pass


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
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
