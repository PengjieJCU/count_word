def main():
    print("please enter a sentence")
    sentence = str(input(""))
    list1 = sentence.split()

    from collections import  Counter
    result = Counter(list1)
    sorted(result.keys())
    print(result)

main()
#hi there
