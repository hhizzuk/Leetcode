class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        #back track --> once res == target push, if res > target go back n try a diff combo

        res = []

        #want to keep track of i
        def backtrack(curr, idx, curr_sum):
            if curr_sum > target: 
                return
            if curr_sum == target:
                res.append(curr.copy())
                return

            for i in range(idx, len(candidates)):
                curr.append(candidates[i])
                backtrack(curr, i, curr_sum + candidates[i])
                curr.pop()

            
        backtrack([], 0, 0)
        return res

    def optimized_CombinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(curr, idx, remain):
            if remain == 0:
                res.append(curr.copy())
                return
            
            for i in range(idx, len(candidates)):
                if candidates[i] > remain:
                    break

                curr.append(candidates[i])
                backtrack(curr, i, remain - candidates[i])
                curr.pop()
        backtrack([], 0, target)
        return res
        
    def diff_CombinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(curr, idx, remain):
            if remain < 0 or idx >= len(candidates):
                return
            if remain == 0:
                res.append(curr.copy())
                return

            curr.append(candidates[idx])
            backtrack(curr, idx, remain - candidates[idx]
            curr.pop()
            backtrack(curr, idx + 1, remain)

        backtrack([], 0, target)
        return res
            
