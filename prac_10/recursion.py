"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n >= 0:
        print(n ** 2)
        do_something(n - 1)


do_something(4)


def calculate_blocks(rows):
    if rows <= 0:
        return 0
    return rows + calculate_blocks(rows - 1)

print(calculate_blocks(2))

