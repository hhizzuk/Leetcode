class Solution:
    #bfs
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        numisland = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '0':
                    continue
                numisland += 1
                queue = deque([[r, c]])
                grid[r][c] = '0'

                while queue:
                    row, col = queue.popleft()
                    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        nr, nc = row + dr, col + dc

                        if (0 <= nr < m and
                            0 <= nc < n and
                            grid[nr][nc] == '1'):
                            grid[nr][nc] = '0'
                            queue.append([nr, nc])
        return numisland



    def stackdfs_numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        numisland = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '0':
                    continue

                #if it's '1'
                numisland += 1
                stack = [(r, c)]
                grid[r][c] = '0'

                while stack:
                    row, col = stack.pop()
                    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, - 1)]:
                        nr, nc = row + dr, col + dc

                        #in bounds
                        if (0 <= nr < m and
                            0 <= nc < n and 
                            grid[nr][nc] == '1'):

                            grid[nr][nc] = '0'
                            stack.append((nr, nc))

        return numisland                        
    #0 1 0
    #1 0 1
    #0 1 0


    def recursdfs_numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        numisland = 0

        def dfs(r, c):
            #out of bounds
            if r < 0 or c < 0 or r >= m or c >= n:
                return
            
            if grid[r][c] == '0':
                return

            grid[r][c] = '0'
            
            dfs(r, c + 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    dfs(r, c)
                    numisland += 1
    
        return numisland
            
    #Recursion, Python calls stack, large grid ccan result to RecursionError when recursion depth exceeds Pythons limit
    #Iteratiev DFS: Manage stack explicity, avoid Pythons recursion depth limit,