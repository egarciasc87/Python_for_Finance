import numpy as np
from copy import deepcopy
import array

def arrayOperartions():
    list1 = [x for x in range(1,5)]
    list2 = [x*2 + 1 for x in range(0,4)]
    list3 = [x*2 for x in range(1,5)]
    list4 = [x*10 for x in range(1,5)]
    array1 = [list1, list2, list3]
    array2 = [deepcopy(list1), deepcopy(list2), deepcopy(list3)]
    print(list4)
    print(array1)
    print(array2)
    print("arrar[0] {}, array[0][1] {}".format(array1[0], array1[0][1]))

    newItem = input("\nEnter new item: ")
    list1[0] = newItem
    print(array1)
    print(array2)

    print("\nArray operations:")
    a = array.array("f", list2)
    print(a)
    a.append(1.5)
    print("Add one new item: ", a)
    a.extend(list3)
    print("Add many items from a list: ", a)
    print(a.tolist())


def numpyOperations():
    list = [x+0.5 for x in range(0,5)]
    print(list)
    a = np.array([x+0.5 for x in range(0,10)])
    print(a)
    print(type(a))
    b = np.array(["a", "b", "c"])
    print(b)
    c = np.array([x*2 for x in range(1,10)])
    d = np.arange(2, 20, 2)
    print(c, d)
    print(c[3:])
    print(c[:3])

    print("\nSummary operations:")
    print("Original array: ", a)
    print("Sum of itmes: ", a.sum())
    print("Standar deviation of items: ", a.std())
    print("Cumulative sum of items: ", a.cumsum())

    print(2 * array.array("f", list))
    print(2 * np.array(list))

    print("\n")
    print(a)
    print(np.exp(a))
    print(np.sqrt(a))


def multipleDimensionOperations():
    a = np.array([x for x in range(0,8)])
    b = np.array([a, a*2])
    c = np.array([a, a*2, a*1.5])
    print(a)
    print(b)
    print(c)

    print("\nOperations on arrays:")
    print("Sum of all items: ", c.sum())
    print("Sum of items by column: ", c.sum(axis=0))
    print("Sum of items by row: ", c.sum(axis=1))



#arrayOperartions()
#numpyOperations()
multipleDimensionOperations()
