# The Torchbearer

**Student Name:** Noah Thao
**Student ID:** 828067299
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
  - SSSP run from S cannot account for globally optimal solutions, ie. worst local cost leading to a overall best cost.

- **What decision remains after all inter-location costs are known:**
  - The lowest cost global path needs to be formed.

- **Why this requires a search over orders (one sentence):**
  - Every order combination provides a different cost, thus every order must be tested to find the minimum.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| Start Node S | Each recorded fuel value is determined from the distance from this node S. |
| Relic Nodes | Least cost between relics needs to be found to form overall lowest cost path|
| Ending Node T | Every node chains together to create a path leading to this ending node T. |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | fuelCosts |
| What the keys represent | Nodes in Graph |
| What the values represent | Fuel costs to reach said node from the start node |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Graph already has calculated distances |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** Dijkstra's is run once for every source node. So with R representing relic nodes, its R + the start node + the exit node = R + 2.
- **Cost per run:** Each run will run Dijkstra's, which has a time complexity of O(V + E (log(V))). So each run costs O(V + E (log(V)))
- **Total complexity:** O((R + 2) * (V+E)log(V)) = O((R)(V+E)log(V)) 
- **Justification (one line):** Total complexity is num of runs * Dijkstra's algorithm time complexity.

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  - Nodes in S have found the shortest possible path from the start node to itself.

- **For nodes not yet finalized (not in S):**
  - Nodes not in S have not found the least cost path and contain the current lowest cost path from the start node.

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  - All nodes are unexplored and contain inf for their values. Inf values for each node is appropriate since no paths have been explored yet.

- **Maintenance : why finalizing the min-dist node is always correct:**
  - Since no negative edge values exist, the possiblity for negative cycles and lower cost paths through multiple iterations is not possible.

- **Termination : what the invariant guarantees when the algorithm ends:**
  - When the algorithm ends, all nodes will be in S and contain the lowest possible cost paths possible from the start node, though the relics nodes, and to the end node.

### Part 3c: Why This Matters for the Route Planner

- By calculating the shortest distances between relic nodes, the start node, and end node, we can start selecting edges to help form the overall lowest cost path.

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** 
  - A Greedy Algorithm would fail for a situation like this since it would pick locally optimal paths to relics but fail to form a globally optimal path.
- **Counter-example setup:** 
  - Say we're working with the following graph:
    {
      'S' : [('R1', 1), ('R2', 3)],
      'R1' : [('V', 2), ('T', 2)],
      'R2' : [('R1', 1), ('T', 4)],
      'V' : [('R2', 2)],
      'T' : []
    }
  - The Greedy Algorithm (G) chooses the lowest-cost relic chamber first
  - The Optimal Algorithm (O) chooses the globally lowest-cost path.
- **What greedy picks:**
  - G will start from S and choose R1. Then it will go R1->V->R2->T. This results in a total cost of 1 + 2 + 2 + 4 = 9
- **What optimal picks:**
  - O will start at S and path to R2 then follow path R2->R1->T, which results in a total cost of 3 + 2 + 2 = 7. 
- **Why greedy loses:** 
  - G chose R1 first since it was the cheapest immediate edge. Though R1 was cheaper than R2, R2's path lead to an overall cheaper path cost compared to R1.

### What the Algorithm Must Explore

- The algorithm must explore different orders of node paths to find the globally optimal path to travel.

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_loc | string | tracks current node. starts with node S |
| Relics already collected | visitedRelics/relics_visited_order | list | Contains explored relics, used for tracking and backtracking|
| Fuel cost so far | currentFuelCost/cost_so_far | float | Used to track the total fuel cost of current path |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | list named visitedRelics/relics_visited_order |
| Operation: check if relic already collected | Time complexity: O(R) where R is number of relics collected|
| Operation: mark a relic as collected | Time complexity: O(1), append the relic to visited list |
| Operation: unmark a relic (backtrack) | Time complexity: O(1), remove relic from the visited and add to separate unvisited list relicsRemaining.|
| Why this structure fits | Relics are added to visitedRelics and returned when path fails or is found, allowing for new path orders to be attempted.|

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** O(K!) where K is the number of relics
- **Why:** Case where each node has a new lower cost/same cost path so every path combination needs to be explored (ie. no pruning occurs).

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

- **What is tracked:** total cost of edges of currently collected nodes and the recorded best cost.
- **When it is used:** The start of the recursive method _explore()
- **What it allows the algorithm to skip:** If the cost of the current order is equal to or exceeds the recorded best cost, then we return and skip that path order.

### Part 6b: Lower Bound Estimation

- **What information is available at the current state:** Explored/unexplored nodes, best recorded cost, current path cost, and distances between source nodes.
- **What the lower bound accounts for:** The lower bound still needs to compare every path combination to find the best cost path.
- **Why it never overestimates:** As stated above, every path combination is still tested against the best found case, so no lower cost paths are disregarded.

### Part 6c: Pruning Correctness

- The pruning condition safe because we're working with guaranteed nonnegative edges, so costs in progress equal to the current best can only cost more and thus can be skipped.
- We stop exploring for the current order if our current path fuel costs is higher than or equal to the recorded best cost
  
---

## References

- GeeksForGeeks.org: Python Lists, Adjacency List in Python, Dijkstra's Algorithm. All articles used to help implement methods in part 2 and in parts 5 and 6. Results were verified by copying each method to a separate .py file and running it with an example graph from the test section of torcherbearer.py (in my case, graph_1 was used for testing for part 2).
- Youtube.com: Dijkstra's Algorithm in 3 minutes (Michael Sambol), Dijkstras Shortest Path Algorithm Explained | With Example | Graph Theory (FelixTechTips). Also just used to help
with understanding Dijkstra's conceptually. 
- GeekForGeeks.org: Multiline String in Python. Literally just used so help format strings of parts 1 and 3 in torchbearer.py.
- ASQ.org: FMEA. Used this article in part 4 briefly to get a better definition of a failure mode.
- GeeksForGeeks.org: Pruning Decision Trees. Used to help with pruning in part 5, mainly conceptual help. Tested methods in separate test.py file using example graphs.
- Referenced my Assignment 7 Graph Problems code to help solve parts 5 and 6 in implmenetation for backtracking. Again, tested methods in a separate test.py file using example graphs in tests section.