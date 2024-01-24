def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        # If the current interval overlaps with the last interval in merged, use the later end time of the two
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            # No overlap, add the current interval
            merged.append(intervals[i])
    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print("Merged Intervals:", merge_intervals(intervals))
