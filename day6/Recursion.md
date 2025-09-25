Here’s a clean, repo-friendly summary you can use as an **explanation/overview section** in your GitHub repo:

---

# Recursion – Overview

**What is Recursion?**
Recursion is the process where a function calls itself (directly or indirectly) to solve a problem by breaking it into smaller subproblems. A recursive function must always have:

* **Base Case:** stopping condition to end recursion.
* **Recursive Case:** smaller subproblem definition.

---

## Key Points

* Each recursive call is stored on the **call stack** → recursion uses more memory.
* Infinite recursion (missing/wrong base case) can cause **stack overflow**.
* Two main types:

  * **Direct recursion:** function calls itself directly.
  * **Indirect recursion:** function calls another function, which calls the original.
* **Tail recursion:** recursive call is the last statement in the function.

---

## Comparison: Recursion vs Iteration

| Aspect      | Recursion                       | Iteration               |
| ----------- | ------------------------------- | ----------------------- |
| Termination | Base case                       | Loop condition          |
| Space       | Needs extra stack memory        | Constant space          |
| Code size   | Shorter, cleaner                | Longer                  |
| Usage       | Natural for tree/graph problems | Simple repetitive tasks |

---

## Common Examples

* **Factorial**: `fact(n) = n * fact(n-1)` with base case `fact(0) = 1`.
* **Sum of Natural Numbers**: Add from `n` down to `0`.
* **Fibonacci Series**: `fib(n) = fib(n-1) + fib(n-2)` with base cases `fib(0)=0`, `fib(1)=1`.
* **Tree/Graph Traversals**: DFS, preorder, inorder, postorder.
* **Divide & Conquer Algorithms**: Merge Sort, Quick Sort, Binary Search.
* **Backtracking**: N-Queens, Sudoku Solver, etc.

---

## Advantages

* Cleaner, simpler code for inherently recursive problems (trees, graphs, divide-and-conquer).
* Useful in **Dynamic Programming** and **Backtracking**.

## Disadvantages

* Higher space/time usage (due to call stack).
* Harder to debug and trace for beginners.

---

✅ **Summary**:
Recursion solves problems by reducing them into smaller subproblems until a base case is reached. It’s powerful for certain algorithms (sorting, searching, traversals, backtracking), but must be used carefully to avoid inefficiency or stack overflow.

---

