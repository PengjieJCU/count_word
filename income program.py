def main():
    income = []
    months = int(input("How many months?"))
    for month in range(1,months+1):
        incomes =float(input("enter income for month"+str(month)+":"))
        income.append(incomes)
    print("\nIncome Report\n")
    total = 0
    for month in range(1,months+1):
        incomes = income[months - 1]
        total +=incomes
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(months, incomes, total))
main()


