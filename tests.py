import heapq

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    explanation = """
- **The failure mode:** 
  - A Greedy Algorithm would fail since it would pick locally optimal paths to relics but fail to form a globally optimal path.

- **Counter-example setup:** 
  - Say we're working with the following graph:
    {
      S : [('R2', 1), ('R1', 4)]
      R1 : [('T', 2)]
      R2 : [('R3', 6)]
      R3 : [('V', 4)]
      R4 : []
      V : [('R4', 9)]
      T : [('R3', 3)]
    }
  - The Greedy Algorithm (G) chooses the closest lowest-cost relic chamber first
  - The Optimal ALgorithm (O) choose the lowest cost path first
- **What greedy picks:**
  - G will start from S and choose R2 to break the stalement of closeness. From there, the path will be R2 -> R3 -> V -> R4, following closest relic
  - G will reach a dead end at R4 and trace back to S, choose S->R1 and finish at T with R1 -> T.
- **What optimal picks:**
  - O will pick the lowest cost edges first, so S -> R2, then R1 -> T, then T -> R3, R3 -> V, S -> R1, and V -> R4 to finish.
- **Why greedy loses:** 
  - In order of path building, G results in fuel costs of 1 + 6 + 4 + 9 + 4 + 2 = 26 while O results in 1 + 2 + 3 + 4 + 9 + 4 = 23
  - G chose R2 first since it was the closest, cheapest edge. Though R2 was cheaper than R1, R1's path lead to an overall cheaper path cost compared to R2.

### What the Algorithm Must Explore
- The algorithm must explore the graph in order of lowest cost between relic chambers first in order to produce a globally optimal output.
    """

    return explanation



def main():
    print(explain_search())

main()