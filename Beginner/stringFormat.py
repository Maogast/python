age = 6000
txt = "The world has existed for {} years since it was created by Jesus"  # The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
print(txt.format(age))



quantity = 3
itemNo = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemNo, price))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))