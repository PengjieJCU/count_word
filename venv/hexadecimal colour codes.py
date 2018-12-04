def main():
    color_code = {'AliceBlue':'#f0f8ff','azure1':'#f0ffff','beige':'#f5f5dc','black':'#000000'}

    color = str(input("Please enter the name of color"))
    if color in color_code:
        print("The code of color is", color_code[color])
    else:
        print("invalid color name")

main()
