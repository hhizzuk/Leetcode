class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        
        res = []
        def backtrack(path, remaining, idx):
            if remaining == 0:
                res.append(path.copy())
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(path, remaining - candidates[i], i + 1)
                path.pop()

        backtrack([], target, 0)
        return res
