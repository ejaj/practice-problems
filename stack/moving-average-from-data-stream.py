from collections import deque


class MovingAverage:
    def __init__(self, k: int):
        """
        Initialize the MovingAverage object with a size k.
        """
        self.k = k  # Window size
        self.window = deque()  # Deque to store sliding window elements
        self.sum = 0  # Sum of elements in the current window

    def next(self, val: int) -> float:
        """
        Calculate the moving average with the new value val.
        """
        # Add the new value to the window
        self.window.append(val)
        self.sum += val

        # If the window size exceeds k, remove the oldest element
        if len(self.window) > self.k:
            removed = self.window.popleft()  # Remove the oldest element
            self.sum -= removed  # Update the sum by subtracting the removed element

        # Return the moving average
        return self.sum / len(self.window)


# Initialize the MovingAverage with a window size of 3
moving_average = MovingAverage(3)

# Add values to the stream and calculate the moving average
print(moving_average.next(1))  # Output: 1.0 (window: [1])
print(moving_average.next(10))  # Output: 5.5 (window: [1, 10])
print(moving_average.next(3))  # Output: 4.67 (window: [1, 10, 3])
print(moving_average.next(5))  # Output: 6.0 (window: [10, 3, 5])
