def main():
    sales = float(input("Enter sales: $"))
    if sales < 1000:
        bonus = sales * 0.1
        print("Your bonus is", bonus)
    elif sales == 1000 or sales > 1000:
        bonus = sales * 0.15
        print("Your bonus is",bonus)

main()
