#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): 2D list representing the island and water.

    Returns:
        int: Perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Each land cell starts with 4 sides
                perimeter += 4

                # Subtract sides for adjacent land cells
                if r > 0 and grid[r - 1][c] == 1:  # Check above
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:  # Check left
                    perimeter -= 2

    return perimeter
