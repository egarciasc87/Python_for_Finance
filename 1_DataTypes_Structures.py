import keyword

def inputInteger():
    number = input("Enter integer:")
    number = int(number)
    print("Number {}, Bit length {}".format(number, number.bit_length()))


def calculate():
    number1 = input("Enter number 1: ")
    number2 = input("Enter number 2: ")
    operation = input("Select operation ([A]dd, [S]ubstract, [M]ultiply, [D]ivision):")
    result = 0
    number1 = int(number1)
    number2 = int(number2)

    if operation == "A":
        result = number1 + number2
    elif operation == "S":
        result = number1 - number2
    elif operation == "M":
        result = number1 * number2
    elif operation == "D":
        result = number1 / number2

    print("result {}, Type {}".format(result, type(result)))


def showKeywords():
    list = keyword.kwlist
    print(list)

    search = "XXX"

    while search != "":
        search = input("Enter string: ")

        if search == "":
            print("End of function...")
        elif search in list:
            print("Included in the list...")
        else:
            print("ERROR: not in the list...")


def textOperations():
    text = input("Enter text: ")
    print("Capital text: ", text.capitalize())

    listWords = text.split()
    print("List of words: ", listWords)

    findText = input("Text to be found: ")
    newText = input("New text: ")
    text = text.replace(findText, newText)
    print("New sentence: ", text)
    print(text.upper())
    print(text.lower())


def numberOperations():
    number = input("Enter number: ")
    number = int(number)

    while number > 0:
        print("number %d" % number)
        print("number {:d}".format(number))
        number = number - 1


def tuplesOperations():
    tuple = (1, 2, "erick", "123", "1")
    print(type(tuple))
    print(tuple)
    search = input("Search element: ")
    print("N° elements: ", tuple.count(search))
    print("Index of -{}-: {}".format(search, tuple.index(search)))


def listsOperations():
    listTest = []
    newItem = "xxx"

    while newItem != "":
        newItem = input("Enter new item: ")

        if newItem != "":
            listTest.append(newItem)

    print(listTest)
    print(type(listTest))
    print(listTest[0])
    listTest.append([3,4])
    print(listTest)
    listTest.extend([3,4])
    print(listTest)
    listTest.insert(2, "erick")
    print(listTest)
    listTest.remove("erick")
    print(listTest)
    listTest.reverse()
    print(listTest)

    print("\nItems of the list:")
    for item in listTest:
        print(item)

    print("\nPow of items:")
    for item in range(2,7):
        print(item ** 2)

    list2 = [i ** 2 for i in range(2,7)]
    list3 = list(map(lambda i: i ** 2, range(2,7)))
    print(list2, list3)


def dictionaryOperations():
    dictPersonalData = { "Name": "Erick",
        "LastName": "Garcia",
        "Country": "Peru",
        "Age": 35}

    print(dictPersonalData)
    field = input("Enter field:")
    print(dictPersonalData[field])
    print("Keys {}, Values {}".format(dictPersonalData.keys(), dictPersonalData.values()))
    print(dictPersonalData.items())

    for key in dictPersonalData.keys():
        print(dictPersonalData[key])


def setOperations():
    item = "XXX"
    set1 = {"erick", "123", "juan", "456"}
    set2 = {"carlos", "1", "erick", "Peru", "456"}

    print(set1.union(set2))
    print(set1.intersection(set2))
    print(set1.difference(set2))


#inputInteger()
#calculate()
#showKeywords()
#textOperations()
#numberOperations()

#tuplesOperations()
#listsOperations()
#dictionaryOperations()
setOperations()
