"""
Problem Statement:
Given an array of meeting time intervals where each interval consists of a start and end time, determine the minimum
number of conference rooms required to hold all the meetings.

Approach:
Separate Start and End Times: Extract the start times and end times of all meetings and sort them separately.
Iterate and Allocate Rooms: Use two pointers to iterate through the start and end times, allocating rooms for new
meetings and freeing up rooms when meetings end.
"""


def min_meeting_rooms(meetings):
    if not meetings:
        return 0

    # Separate and sort start and end times
    start_times = sorted([meeting[0] for meeting in meetings])
    end_times = sorted([meeting[1] for meeting in meetings])
    print(start_times)
    print(end_times)

    # Use two pointers to iterate through start and end times
    start_pointer, end_pointer = 0, 0
    rooms_needed = 0
    max_rooms = 0
    while start_pointer < len(meetings):
        # If the next meeting starts before the current one ends,
        # we need a new room
        if start_times[start_pointer] < end_times[end_pointer]:
            rooms_needed += 1
            start_pointer += 1
        else:
            # Otherwise, a meeting has ended and we can reuse a room
            rooms_needed -= 1
            end_pointer += 1
        # Update the maximum rooms needed so far
        max_rooms = max(max_rooms, rooms_needed)

    return max_rooms


meetings = [[0, 30], [5, 10], [15, 20]]
print("Minimum meeting rooms needed:", min_meeting_rooms(meetings))
