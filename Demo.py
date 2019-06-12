listvar = [10, 20 , 30, "Apple", "Banana", "Cherry"]


def lengthlist(listvar):
 count = 0
 for x in listvar:
    count = count + 1
 return count
#print("The length of list is", lengthlist(listvar))


i = lengthlist(listvar) - 1
while i>=0:
    print(listvar[i])
    i = i - 1