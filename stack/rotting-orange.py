from collections import deque


def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])

    queue = deque()
    fresh_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh_count += 1
    # print(queue)
    # print(fresh_count)
    minutes = 0
    while queue:
        r, c, minutes = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh_count -= 1
                queue.append((nr, nc, minutes + 1))

    return -1 if fresh_count > 0 else minutes


grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

# Run the function
result = orangesRotting(grid)
