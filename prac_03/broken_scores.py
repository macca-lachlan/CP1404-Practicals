"""
CP1404/CP5632 - Practical 01
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(determine_result(score))


def determine_result(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 50 and score < 90:
        result = "Passable"
    elif score >= 90 and score <= 100:
        result = "Excellent"
    else:
        result = "Bad"
    return result

main()
