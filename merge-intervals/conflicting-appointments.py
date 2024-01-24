"""
Problem Statement:
Given an array of intervals representing appointment times, check if any of the appointments overlap.
Each interval is a pair of two numbers, representing the start and end times of an appointment.
Approach:
Sort Appointments: First, sort the appointments based on their start times.
This allows us to compare each appointment with the next one in a sequential manner.
Check for Overlap: Iterate through the sorted intervals and check if the end time of an appointment is greater
than the start time of the next appointment. If so, there is a conflict.
"""


def can_attend_all_appointments(appointments):
    # Sort appointments by start time
    appointments.sort(key=lambda x: x[0])
    # Iterate through the appointments
    for i in range(1, len(appointments)):
        if appointments[i][0] < appointments[i - 1][1]:
            # There is a conflict
            return False
    # No conflicts found
    return True


appointments = [[1, 4], [2, 5], [7, 9]]
print("Can attend all appointments:", can_attend_all_appointments(appointments))
