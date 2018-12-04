def main():
    score = float(input("Enter score: "))
    if score> 100 or score < 0:
        print("invalid score")
    else:
        if score > 50 or score == 50:
            print("Passable")
        if score > 90 or score == 90:
            print("Excellent")
        if score < 50:
            print("Bad")
main()
