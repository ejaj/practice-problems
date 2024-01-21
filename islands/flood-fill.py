"""
You are given a 2D grid (image) where each cell represents a pixel with a specific color (represented as a number). You are also given a starting pixel (row and column) and a new color.
The task is to fill the connected component of the starting pixel with the new color.
"""


def flood_fill(image, sr, sc, new_color):
    rows, cols, original_color = len(image), len(image[0]), image[sr][sc]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
            return
        image[r][c] = new_color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    if original_color != new_color:
        dfs(sr, sc)
    return image


image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr, sc, newColor = 1, 1, 2
print(flood_fill(image, sr, sc, newColor))
