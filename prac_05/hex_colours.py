COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Beige": "#f5f5dc", "Black": "#000000",
                "BlanchedAlmond": "#ffebcd", "Blue1": "#0000ff", "DarkViolet": "#9400d3", "DarkOrchid": "#9932cc",
                "DeepSkyBlue1": "#00bfff", "ForestGreen": "#228b22"}

colour = input("Please enter a colour name: ")
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "is", COLOUR_CODES[colour])
    else:
        print("Invalid Colour Code")
    colour = input("Please enter a colour name: ")

# for colour, code in COLOUR_CODES.items():
#     print("{} is {}".format(colour, code))

