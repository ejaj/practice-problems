def has_cycle(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(r, c, pr, pc):
        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) == (pr, pc):
            return False
        if visited[r][c]:
            return True
        visited[r][c] = True
        # Assume we can move in all four directions; adjust as per the problem's constraints
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr != pr or nc != pc:  # Avoid going back to the parent cell directly
                if dfs(nr, nc, r, c):
                    return True
        visited[r][c] = False  # Backtrack
        return False

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and dfs(i, j, -1, -1):
                return True
    return False


# Example usage
matrix = [[1, 2], [3, 4]]
print("Does the matrix have a cycle?", has_cycle(matrix))
