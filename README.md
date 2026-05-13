# The Torchbearer

**Student Name:** Noah Thao
**Student ID:** 828067299
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  - SSSP run from S only provides shortest paths to chamber nodes but doesn't provide shortest paths between chambers.

- **What decision remains after all inter-location costs are known:**
  - The lowest cost path between two relics is chosen first.

- **Why this requires a search over orders (one sentence):**
  - Every order combination provides a different cost, thus every order must be tested to find the minimum.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| Start Node S | Each fuel value is determined from the distance from this node S. |
| Relic Nodes | Fuel values are updated during edge relaxation between other relic nodes and the start node. |
| Ending Node T | Every node chains together to create a path leading to this ending node T. |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | fuelCosts |
| What the keys represent | Nodes, specifically relics |
| What the values represent | Fuel costs to reach said node from the start node |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Graph already contains lowest cost path to use|

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** Dijkstra's is run once for every source node. So with R representing relic nodes, its R + the start node + the exit node = R + 2.
- **Cost per run:** Each run will run Dijkstra's, which has a time complexity of O(V + E (log(V))). So each run costs O(V + E (log(V)))
- **Total complexity:** O((R + 2) * (V+E)log(V))
- **Justification (one line):** Total complexity is num of runs * Dijkstra's algorithm time complexity; can be formally represented as O((R)(V+E)log(V)) 

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  - Nodes in S have found the shortest possible path from the start node to itself.

- **For nodes not yet finalized (not in S):**
  - Nodes not in S have not found the least cost path and contain the current lowest cost path from the start node.

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  - All nodes are unexplored and contain inf for their values. Inf values for each node is appropriate since no paths have been explored yet.

- **Maintenance : why finalizing the min-dist node is always correct:**
  - Since no negative edge values exist, the possiblity for negative cycles and lower cost paths through multiple iterations is not possible.

- **Termination : what the invariant guarantees when the algorithm ends:**
  - When the algorithm ends, all nodes will be in S and contain the lowest possible cost paths possible from the start node, though the relics nodes, and to the end node.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

- By calculating the shortest distances between relic nodes, the start node, and end node, we are able to decide which edge to start with when building the path.

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- GeeksForGeeks.org: Python Lists, Adjacency List in Python, Dijkstra's Algorithm. All articles used to help implement methods in part 2. Results were verified by copying each method
to a seperate .py file and running it with an example graph from the test section of torcherbearer.py (in my case, graph_1 was used for testing).
- Youtube.com: Dijkstra's Algorithm in 3 minutes (Michael Sambol), Dijkstras Shortest Path Algorithm Explained | With Example | Graph Theory (FelixTechTips). Also just used to help
with understanding Dijkstra's conceptually. 
- GeekForGeeks.org: Multiline String in Python. Literally just used so help format strings of parts 1 and 3 in torchbearer.py.