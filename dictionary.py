import os
import dModule


myDict = dict()

while True:

    print("""
    English - Uzbek
1 - Add new word
2 - Search word
3 - Update word
4 - Delete word
5 - Show all words
6 - Clear window
0 - Exit""")

    try:
        print()
        choice = int(input("Enter the number: "))
        print()
    except ValueError:
        print()
        print("Error. You should enter an integer number. Please try again.")
        continue

    if choice == 1:
        myDict = dModule.add(myDict)
    elif choice == 2:
        dModule.search(myDict)
    elif choice == 3:
        myDict = dModule.update(myDict)
    elif choice == 4:
        myDict = dModule.delete(myDict)
    elif choice == 5:
        dModule.show(myDict)
    elif choice == 6:
        os.system("clear")
    elif choice == 0:
        dModule.exit()
        break
    else:
        print("Unknown operation. Please try again.")