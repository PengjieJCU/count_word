def main():
    numbers = []
    for i in range(5):
        number = int(input("please enter five numbers"))
        numbers.append(number)
    print("the first number is",numbers[0])
    print("the last number is", numbers[-1])
    print("the smallest number is",min(numbers))
    print("the largest number is",max(numbers))
    print("the average number is", sum(numbers)/len(numbers))
    print(numbers)



main()
