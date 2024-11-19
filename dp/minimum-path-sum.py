"""
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""


def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    
    # Update the first row: can only move right
    for j in range(1, n):
        grid[0][j] += grid[0][j-1]
        
    # Update the first column: can only move down

    for i in range(1, m):
        grid[i][0] += grid[i-1][0]    
        
    # Update the rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    return grid[m - 1][n - 1]

grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

print("Minimum Path Sum:", minPathSum(grid))