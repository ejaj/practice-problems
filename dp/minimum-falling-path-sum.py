def min_falling_path_sum(matrix):
    n = len(matrix) 
    for row in range(n - 2, -1, -1):  # Loop from second-to-last row to the top row
        for col in range(n):
           # Calculate the minimum of three possible paths from the row below
            straight_down = matrix[row + 1][col]
            diagonal_left = matrix[row + 1][col - 1] if col > 0 else float('inf')  # Boundary check
            diagonal_right = matrix[row + 1][col + 1] if col < n - 1 else float('inf')  # Boundary check
            
            matrix[row][col] += min(straight_down, diagonal_left, diagonal_right)
    return min(matrix[0])

matrix1 = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
min_falling_path_sum(matrix1)