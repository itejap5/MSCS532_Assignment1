# MSCS532 Assignment 1

This repository contains my Python program for Assignment 1.

The program uses the Insertion Sort algorithm to sort an array in monotonically decreasing order. Insertion Sort works like sorting playing cards in your hand. It starts from the second number and compares it with the numbers before it.

For decreasing order, the bigger number should move toward the front. This line is the most important part:

```while i >= 0 and arr[i] < key:```

It means:

- While the number on the left is smaller than the current number, move it to the right.

- That is why the final list becomes biggest to smallest.

## File Included

- insertion_sort_descending.py

## How to Run

Use this command in the terminal:

```bash
python insertion_sort_descending.py
```

### Example Output:

Original array:
[31, 41, 59, 26, 41, 58]

Sorted array in decreasing order:
[59, 58, 41, 41, 31, 26]