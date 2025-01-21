# def getMaxThroughput(host_throughput):
#     # Step 1: Initialize total throughput
#     total_throughput = 0
#
#     # Step 2: Form clusters of 3 servers
#     clusters = []
#     while len(host_throughput) >= 3:
#         # Select the first, second, and third elements for a cluster
#         cluster = [host_throughput.pop(0), host_throughput.pop(1), host_throughput.pop(-1)]
#         clusters.append(cluster)
#         median = sorted(cluster)[1]  # Find the median
#         total_throughput += median
#
#     # Step 3: Return the total throughput
#     return total_throughput
#
#
# # Example usage:
# host_throughput = [8, 6, 3, 4, 4, 5, 6]
# print(f"Final Total Throughput: {getMaxThroughput(host_throughput)}")  # Output: 11
#
#


def getMaxThroughput(host_throughput):
    # Step 1: Sort the throughput values in descending order
    host_throughput.sort(reverse=True)

    # Step 2: Initialize total throughput
    total_throughput = 0

    # Step 3: Form clusters of size 3
    for i in range(0, len(host_throughput) - 2, 3):  # Ensure only full clusters of 3 are formed
        cluster = host_throughput[i:i+3]  # Take 3 elements at a time
        median = cluster[1]  # Median is the 2nd largest value (array is sorted)
        total_throughput += median

    # Step 4: Return the total throughput
    return total_throughput


# Example usage:
host_throughput = [279, 744, 508, 961, 13, 599, 996, 391]
print(f"Final Total Throughput: {getMaxThroughput(host_throughput)}")
