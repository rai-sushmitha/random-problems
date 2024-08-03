Dynamic Programming (DP) 
- is a method used in mathematics and computer science to solve complex problems by breaking them down into simpler subproblems.

How Does Dynamic Programming (DP) Work?
  - Identify Subproblems: Divide the main problem into smaller, independent subproblems.
  - Store Solutions: Solve each subproblem and store the solution in a table or array.
  - Build Up Solutions: Use the stored solutions to build up the solution to the main problem.
  - Avoid Redundancy: By storing solutions, DP ensures that each subproblem is solved only once, reducing computation time.

Problems:
  - Fibonacci sequence
  - Longest common subsequence (finding the longest subsequence that is common to two strings)
  - Shortest path in a graph (finding the shortest path between two nodes in a graph)
  - Knapsack problem (finding the maximum value of items that can be placed in a knapsack with a given capacity)
  - Matrix Chain Multiplication

Approaches of Dynamic Programming (DP)
1. Top-Down Approach (Memoization):
  -  Starts with the final solution and recursively breaks it down into smaller subproblems.
  -  Stores the solutions to subproblems in a table to avoid redundant calculations.
  -  Suitable when the number of subproblems is large and many of them are reused.

2. Bottom-Up Approach (Tabulation):
  - Starts with the smallest subproblems and gradually builds up to the final solution.
  - Fills a table with solutions to subproblems in a bottom-up manner.
  - Suitable when the number of subproblems is small and the optimal solution can be directly computed from the solutions to smaller subproblems.
