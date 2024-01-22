def has_cycle(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()  # To keep track of visited cells

    def dfs(r, c, start, char, path):
        if (r, c) in path and (r, c) != start:
            return False  # If we hit a cell already in the current path, it's not a cycle
        if (r, c) == start and len(path) > 0:
            return True  # If we return to start and have traveled, it's a cycle

        path.add((r, c))  # Add current cell to path
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Possible directions to move
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char and (nr, nc) not in visited:
                if dfs(nr, nc, start, char, path):
                    return True
        path.remove((r, c))  # Remove cell from path when backtracking
        visited.add((r, c))  # Mark cell as visited
        return True

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited and dfs(i, j, (i, j), grid[i][j], set()):
                return True  # If any cell starts a cycle, return True


grid = [["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]
print("Is there a cycle?", has_cycle(grid))
