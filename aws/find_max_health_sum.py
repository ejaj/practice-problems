from collections import defaultdict
def findMaxHealthSum(health, serverType, m):


    # Group health by server type
    server_health = defaultdict(list)
    for h, t in zip(health, serverType):
        server_health[t].append(h)

    # Calculate the total health for each server type
    type_sums = []
    for t in server_health:
        type_sums.append(sum(server_health[t]))

    # Sort the sums in descending order and pick the top m types
    type_sums.sort(reverse=True)

    # Take the top m sums and return their total
    return sum(type_sums[:m])


# Example usage:
health = [4, 5, 5, 6]
serverType = [1, 2, 1, 2]
m = 1
print(findMaxHealthSum(health, serverType, m))  # Output: 11
