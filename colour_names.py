COLOUR_NAMES = {"AliceBlue": "#f0f8ff", "BlanchedAlmond": "#ffebcd", "chocolate": "#d2691e", "coral3": "#cd5b45", "DarkOliveGreen2": "#bcee68"}

def main():
    colour_name = str(input("WHat is the colour name?"))
    if colour_name in COLOUR_NAMES:
        print("{}".format(COLOUR_NAMES[colour_name]))
    else:
        print("Error")

main()