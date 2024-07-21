class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        ROW, COL = len(maze), len(maze[0])
        
        visited = set()
        visited.add((entrance[0],entrance[1]))
        
        queue = deque([(entrance[0], entrance[1], 0)])
        
        directions = [(1,0), (0,1), (-1,0),(0,-1)]
        
        while queue:
            r, c, steps = queue.popleft()
            
            if (r == 0 or r == ROW - 1 or c == 0 or c == COL -1) and (r,c) != (entrance[0],entrance[1]):
                return steps
            
            for rdir, cdir in directions:
                nr, nc = r+rdir, c+cdir
                if 0<=nr<ROW and 0<=nc<COL and (nr, nc) not in visited and maze[nr][nc] == ".":
                    queue.append((nr, nc, steps+1))
                    visited.add((nr, nc))
        
        return -1