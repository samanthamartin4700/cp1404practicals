"""
CP1404 HEX_COLOURS
By Samantha Martin
"""

COLOURS = {"coral": "#ff7f50", "DarkSalmon": "#e9967a", "DarkSeaGreen2": "#b433b4", "OliveDrab2": "#b3ee3a",
           "pale": "#db7093", "PaleGreen3": "#7ccd7c", "PaleTurquoise3": "#96cdcd", "PaleVioletRed": "#db7093",
           "pink": "#ffc0cb", "plum": "#dda0dd"}

colour_name = input("Enter colour name: ")
for name in COLOURS:
    if colour_name in COLOURS:
        print(COLOURS[colour_name])
        colour_name = input("Enter colour name: ")
    elif colour_name == "":
        print("Goodbye :)")
        break
    elif colour_name not in COLOURS:
        print("Invalid name. Please try again :)")
        colour_name = input("Enter colour name: ")