# Development Log – The Torchbearer

**Student Name:** Noah Thao
**Student ID:** 828067299
---

## Entry 1 – [5/11/2026]: Initial Plan.
The plan is probably just to go in order with each part in order. From what I went over, the hardest parts are going to be the actual implementation of Dijktra's and the MST bottom
up implementation. Also thinking of testing each method individually in a separate .py file for easier organiation and testing. Time to test commit

---

## Entry 2 – [5/12/2026]: Finished up part 2
Implemented part 2. Ran into issues when implementing Dijkstra's initially, mostly in regards to syntax for accessing elements in the
adjacency list. Read some articles and watched some youtube videos to see how they worked. Also got stumped for a second with the precompute method, 
figured it out by looking over the parameters for a bit. Mainly testing everything on a different file test.py and using example graphs from torchbearer.py as input. 
Also just realized I accidentally committed test.py and assignment.md to the repo; gonna remove before submission.

---

## Entry 3 – [5/12/2026]: Reassessing the problem and editing part 1

Realized I incorrectly interpreted and answered section 1 after implementing and understanding section 2. I initially thought we were going to do edge selection and prove why path building was wrong but realized we're using both together for the solution after completing 2.3. Rewrote the answers in part 1.

---

---

## Entry 4 – [5/13/2026]: Fixed part 1 in torchbearer and finished part 3
Finished writing out part 3. Again, instructions are very clean and minimal so I personally had bit of a hard time analyzing the question. Got it down eventually though.
Also restructured some explanation strings for parts 1 and 3 in torchbearer.py for visual clarity.

---

---

## Entry 5 – [5/13/2026]: Finished up part 4
Finished writing part 4. Took me a bit to figure what specifically a failure mode is and how to word it properly but was able to figure it out after going over an article. 
Every other section of part 4 was fine; experience from practice midterm 2 and the real midterm 2 helped with forming the rest of the proof.

---

---

## Entry 6 – [5/14/2026]: Finished parts 5, 6, (and 7 technically) and updated parts 1, 4
This took forever but I completed parts 5 and 6. The conceptual aspect in README was not that bad but the implementation took a while to figure out. Retracing my steps from
the N-Queens and Graph Coloring algorithm from assignment 7 helped me with the backtracking aspect of part 6. Also looked over part 4 and noticed that my counterexample and algorithm determination is not correct and changed both. Also edited errors in part 1. Gonna do final touches after and maybe 1 or 2 more commits before submission

---

## Entry 7 – [5/14/2026]: Post-Implementation Reflection


All finished I believe. Forgot to update written answers from README.md to torchbearer.py so I went ahead and did that for parts 1, 3, and 4. I was gonna delete test.py and ASSIGNMENT.md since I didn't know if it follows the deliverables section but decided to leave them in just so my testing explanation somewhat makes sense. I think I could improve parts 5 and 6; certain Python methods and functions could likely be used to clean up number of variables and relic tracking methods. Visual clarity could also be improved.

---

## Final Entry – [5/14/2026]: Time Estimate

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 2 hours |
| Part 2: Precomputation Design | 2 hours |
| Part 3: Algorithm Correctness | 1 hour |
| Part 4: Search Design | 2 hours |
| Part 5: State and Search Space | 3 hours|
| Part 6: Pruning | 3 hours |
| Part 7: Implementation | 11 hours |
| README and DEVLOG writing | 7 hours|
| **Total** | 18 hours |

Just for clarification, implementation and writing are sums of each section I spent time on. For example, pruning took me about 3 hours to figure out, but 2 of them
were spent on implementation and around 1 was spent on writing.