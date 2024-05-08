# Sliding Window Technique

The sliding window technique is a method used in algorithm design to efficiently solve problems related to arrays and
lists. By moving a window over the data set, we can manage and analyze subsets of data sequentially.

## Basic Concept

Think of a scenario where you have a queue of people and need to analyze every group of three consecutively. You start
with the first three people, perform your analysis, then slide your window one person forward to include the next person
in line, and so on.

## Key Features

1. **Efficiency**: Instead of recalculating everything, you update your analysis by removing the data of the element
   exiting the window and adding the data of the new element entering it.
2. **Fixed or Variable Size**: The window can have a fixed size (like three people from our example) or a variable
   size (such as finding the longest substring without repeating characters).
3. **Applications**: This technique is useful for tasks like finding maximum or minimum values in a subarray, checking
   for substrings, or calculating moving averages.

## Example

Consider an array `[1, 3, -1, 5, 3, 6, 7]`. If you need to find the maximum number for every three consecutive numbers
using the sliding window technique:

- **First Window**: `[1, 3, -1]` -> Max is 3
- **Slide the window right**: `[3, -1, 5]` -> Max is 5
- **Next Slide**: `[-1, 5, 3]` -> Max is 5
- Continue this until the end of the array.

## References

- GeeksforGeeks. (n.d.). Sliding Window Maximum (Maximum of all subarrays of size k). Retrieved
  from [GeeksforGeeks](https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/)
- Wikipedia. (2022). Window function. Retrieved from [Wikipedia](https://en.wikipedia.org/wiki/Window_function)

This method reduces time complexity compared to evaluating every set of three numbers separately.
