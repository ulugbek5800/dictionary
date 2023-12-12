# data.keys() - eng, data.values() - uzb
# search - try ; update, delete - '0','1'

def add(data):
    word = [input("Eng -> ").lower(), input("Uzb -> ").lower()]
    data[word[0]] = word[1]
    print()
    print("{} - {} (eng-uzb)".format(word[0], word[1]))
    print("New word was added successfully!")
    return data
    # return input("Eng -> ").lower(), input("Uzb -> ").lower()


def search(data):
    check = True
    while check:
        word = input("Enter the word to search (eng or uzb): ").lower()
        #print(data)

        if word in data.keys():
            print()
            print(f"{word} - {data[word]} (eng-uzb)")
        elif word in data.values():
            for i in data.items():
                if i[1] == word:
                    print()
                    print(f"{i[1]} - {i[0]} (uzb-eng)")
        else:
            print("There is no such word in dictionary.")

            while True:
                try:
                    check = int(input("Enter 1 to search again, 0 to exit: "))
                    if check == 1 or check == 0:
                        break   # the loop will break only if there is no an error
                    else:
                        print("Error. Please try again.")
                except ValueError:
                    print("Error. Please try again.")

            continue            # necessary

        print()
        while True:
            try:
                print("Do you want to search another word?")
                check = int(input("1 - yes, 0 - no: "))
                if check == 1 or check == 0:
                    print()
                    break       # goes to the main while
                else:
                    print("Error. Please try again.")
            except ValueError:
                print("Error. Please try again.")


def update(data):
    check = True        # check is important here
    temp = list()

    while check:
        word = input("Enter the word to update (eng or uzb): ").lower()
        if word in data.keys():     # if data.get(word):
            #print(f"{word} - {data[word]} (eng-uzb)")
            temp.append(word)
            temp.append(data[word])
            break
        elif word in data.values():
            for i in data.items():
                if i[1] == word:
                    #print(f"{i[1]} - {i[0]} (uzb-eng)")
                    temp.append(i[0])
                    temp.append(i[1])
                    break
            break
        else:
            print("There is no such word in dictionary.")

            while True:
                check = input("Enter 1 to try again, 0 to exit: ")
                if check == '1' or check == '0':
                    check = int(check)
                    break
                else:
                    print("Error. Please try again.")
            continue            # not necessary

    if check:
        print()
        print(f"{temp[0]} - {temp[1]} (eng-uzb)")
        print()
        data.pop(temp[0])       # u should do this before temp[0] (key) is changed
        
        while True:
            print("Which word do you want to change?")
            change = input("0 - 'eng', 1 - 'uzb': ")
            if change == '0':
                temp[0] = input("Enter new word (eng): ")
            elif change == '1':
                temp[1] = input("Enter new word (uzb): ")
            else:
                print("Error. Try again.")
                continue
            break

        data[temp[0]] = temp[1]
        print()
        print("{} - {} (eng-uzb)".format(temp[0], temp[1]))
        print("The word was changed successfully!")

    return data


def delete(data):
    check = True
    while check:
        word = input("Enter the word to delete (eng or uzb): ").lower()
        if word in data.values():
            for i in data.items():
                if i[1] == word:
                    word = i[0]
                    break

        if word in data.keys():
            print()
            print(f"{word} - {data[word]} (eng-uzb)")
            print()
            while True:
                print("Are you sure you want to delete this word?")
                check = input("Enter 1 to delete, 0 to cancel: ")
                if check == '1' or check == '0':
                    check = int(check)
                    break
                else:
                    print("Error. Please try again.")
            break

        else:
            print("There is no such word in dictionary.")
            while True:
                check = input("Enter 1 to try again, 0 to exit: ")
                if check == '1' or check == '0':
                    check = int(check)
                    break
                else:
                    print("Error. Please try again.")
            continue            # not necessary

    if check:
        data.pop(word)
        print("The word was deleted successfully!")
    return data


def show(data):
    if data != {}:
        print("All words (eng-uzb):")
        for i in data.items():
            #print(i)
            print("{} - {}".format(i[0], i[1]))
    else:
        print("dictionary is empty...")


def exit():
    print("Bye :)")
