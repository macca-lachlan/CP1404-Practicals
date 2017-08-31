
HEX_COLOURS = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "AQUAMARINE": "#7fffd4", "AZURE": "#f0ffff",
               "BEIGE": "#f5f5dc", "BISQUE": "#ffe4c4", "BLACK": "#000000", "BLUE": "#0000ff", "BROWN": "a52a2a"}

colour = input("Enter a colour: ")
while colour != "":
    if colour.upper() in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour.upper()])
    else:
        print("Invalid colour")
    colour = input("Enter a colour: ")

