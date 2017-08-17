"""
CP1404/CP5632 - Practical 01
Broken program to determine score status
"""


# score = float(input("Enter score: "))
# if score < 0:
#    print("Invalid score")
# else:
#    if score > 100:
#        print("Invalid score")
#    if score > 50:
#        print("Passable")
#    if score > 90:
#        print("Excellent")
# if score < 50:
#    print("Bad")

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 50 and score < 90:
    print("Passable")
elif score >= 90 and score <= 100:
    print("Excellent")
else:
    print("Bad")
