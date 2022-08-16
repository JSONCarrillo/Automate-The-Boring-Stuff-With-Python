import re

from pip import main

# -- SECTION 1 --
print("Section 1: Creating Regex Objects \n")

# sets the regex pattern
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# using the regex pattern, the search method looks for a section of string that matches the given pattern
matchObject = phoneNumRegex.search("Give me a call at 415-123-1234")

print("Phone Number: {}".format(matchObject.group()))

# -- SECTION 2 --
print("\nSection 2: More Pattern Matching\n")

phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchObject2 = phoneNumRegex2.search("Give me a call at 415-123-1234")
print("Group 1: {0}\nGroup 2: {1}\nGroup 3: {2}\n".format(matchObject2.group(0), matchObject2.group(1), matchObject2.group(2)))

# groups method splits the 2 groups encapsulated in parenthesis as as tuple
# areaCode and mainNumber are then assigned the respective section of the tuple
areaCode, mainNumber = matchObject2.groups()
print("Area Code: {0}\nMain Number: {1}\n".format(areaCode,mainNumber))

# -- SECTION 3 --
print("Section 3: Multiple Groups with Pipe \n")

# Setsup the regular expression object
heroRegex = re.compile(r'Batwoman|Selina Gomez')

#searches for the above regex within the phrase
mo = heroRegex.search("This movie stars Selina Gomez as Batwoman!")
# prints the first match which should be Selina Gomez
print(mo.group())

mo1 = heroRegex.search("This movie is called Batwoman and stars Selina Gomez")
# this should print batwoman
print(mo1.group())

# By encapsulating the Regex into a parenthesis, it allows for the required 'Bat' and the optional items within the parenthesis
batRegex = re.compile(r'Bat(Mobile|Man|arang)')
mo2 = batRegex.search('I\'m BatMan')
mo3 = batRegex.search('Get in the BatMobile')
mo4 = batRegex.search('Throw the Batarang')

print(mo2.group())
print(mo3.group())
print(mo4.group())