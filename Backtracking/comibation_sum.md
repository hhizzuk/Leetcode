# Combination Sum

**LeetCode:** [39. Combination Sum](https://leetcode.com/problems/combination-sum/)

**Difficulty:** Medium

**Topic:** Backtracking

**Status:** Solved / Needs Review

## 1. Initial Approach

My initial thought process:
- Use backtracking to explore different combinations.
- Keep track of the current sum.
- If the sum exceeds the target, backtrack.
- If the sum equals the target, add the combination to the results.

## 2. My Attempt

See [combination_sum.py](combination_sum.py).

## 3. Complexity Analysis

- **Time:** O(n^(T/m))
- **Space:** O(T/m)

N = number of candidates
T = target
m = smallest candidate, smallest candidate determines maximum possible recursion depth

In combination sum, can reuse candidates so same number can be added multiple times
[T/m]

## 4. Improvements

What could be optimized?
- Sort the candidates so you can stop exploring when sum exceeds target [ never specified in rules that it'll always be sorted]
- switching curr_sum to track how much target remains

## 5. Takeaways

What I learned:
- use curr.copy() when storing because curr is modified aterwards
- 

## 6. Review Notes

What I struggled with:
- 

What I should remember next time:
- 