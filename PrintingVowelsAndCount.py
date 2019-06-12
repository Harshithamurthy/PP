# def Vowel(Text):
#     vowels = "aeiouAEIOU"
#     print(len([Letter for Letter in Text if Letter in vowels]))
#     print([Letter for Letter in Text if Letter in vowels])
#
# Vowel("Print the count and vowels in a string");
#
#
# #OR
#
#
# String = input("Enter the String")
# vowels = "aeiouAEIOU"   # or vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# list = []
#
# for x in String:
#     if x in vowels:
#         list.append(x)
# print(list)
# print(len(list))


#OR

vowels = ['a', 'e', 'i', 'o', 'u']
element = input("Enter the element")
data = set(element)
result = data.intersection(vowels)
print(result)
