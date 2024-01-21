"""
You are given a 2D grid (matrix) where each cell has either a 1 (land) or a 0 (water). An island is formed by connected
lands (1's) horizontally or vertically (but not diagonally). The task is to count the number of distinct islands in the grid.
Input:
11000
11000
00100
00011
Output:
3
Two islands formed by the first two rows (11000, 11000).
One island formed by the last two 1s in the bottom row (00011).
"""


def num_islands(grid):
    if not grid:
        return 0

    def dfs(i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'  # Mark as visited
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count


# Example usage
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print("Number of islands:", num_islands(grid))
