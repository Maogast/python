myList = ["Genesis","Revelation", 34, True ]
print(type(myList),myList, len(myList), myList[3])


if "Genesis" in myList:
    print("Yea , i got you Genesis")
else:
    print ("Nay next time")    
    
    myList = ["Genesis","Revelation", 34, True ]
    myList[3] = "False"
    print(myList)