import math


class Node:
    def __init__(self, point, axis=None, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right


def distance(point1, point2):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(point1, point2)]))


def build_kdtree(points, depth=0):
    if not points:
        return None

    k = len(points[0])
    axis = depth % k

    sorted_points = sorted(points, key=lambda x: x[axis])

    median_idx = len(sorted_points) // 2
    median_point = sorted_points[median_idx]

    return Node(
        point=median_point,
        axis=axis,
        left=build_kdtree(sorted_points[:median_idx], depth + 1),
        right=build_kdtree(sorted_points[median_idx + 1:], depth + 1)
    )


def insert(root, point, depth=0):
    if root is None:
        return Node(point)

    k = len(point)
    axis = depth % k

    if point[axis] < root.point[axis]:
        root.left = insert(root.left, point, depth + 1)
    else:
        root.right = insert(root.right, point, depth + 1)

    return root


def nearest_neighbor_search(root, query_point, depth=0, best=None):
    if root is None:
        return best

    if best is None or distance(query_point, root.point) < distance(query_point, best):
        best = root.point

    axis = depth % len(query_point)
    if query_point[axis] < root.point[axis]:
        next_node = root.left
        opposite_node = root.right
    else:
        next_node = root.right
        opposite_node = root.left

    best = nearest_neighbor_search(next_node, query_point, depth + 1, best)

    if opposite_node is not None and abs(query_point[axis] - root.point[axis]) < distance(query_point, best):
        best = nearest_neighbor_search(opposite_node, query_point, depth + 1, best)

    return best


# Example usage
points = [(7, 2), (5, 4), (9, 6), (2, 3), (8, 1), (4, 7)]
query_point = (6, 5)

# Build the K-D tree
root = build_kdtree(points)

# Insert a new point
new_point = (6, 3)
root = insert(root, new_point)

# Perform nearest neighbor search
nearest_point = nearest_neighbor_search(root, query_point)

print("Query Point:", query_point)
print("Nearest Neighbor Point:", nearest_point)
