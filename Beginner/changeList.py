myList = ["Genesis","Revelation", 34, True ]
myList[3] = "False"
print(myList)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["concotion", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist.insert(2, "pineapple")
thislist.append("ConcotionOfJagari")
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
myList = ["Genesis","Revelation", 34, True ]
thislist.extend(myList)    #To append elements from another list to the current list, use the extend() method.
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")  # tuple has brackets ()
thislist.extend(thistuple)
print(thislist)

