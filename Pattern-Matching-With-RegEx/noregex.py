# So, let's say you are wanting to
# get a phone number, but without using
# regular expression, you can do so by creating the 
# following function

def isPhoneNumber(num):
    if len(num) != 12:
        return False

    for i in range(0,3): # checks if the area code is all numbers
        if not num[i].isdecimal(): 
            return False
    
    for i in range(4,7): # checks if the 2nd block in the phone number is all numbers
        if not num[i].isdecimal():
            return False

    for i in range(8,12): # checks if the 3rd block in the phone number is all numbers
        if not num[i].isdecimal():
            return False

    if num[3] != '-' or num[7] != '-': # Checks that there is a hyphen at the 3rd and 7th index of the number
        return False


    return True

# A list of tests to make sure our function works
print("Is 415-123-1234 a phone number?") # True
print(isPhoneNumber("415-123-1234"))
print("Is 415-123-123a a phone number?") # False
print(isPhoneNumber("415-123-123a"))
print("Is 415-12a-1235 a phone number?") # False
print(isPhoneNumber("415-12a-1235"))
print("Is a15-123-1235 a phone number?") # False
print(isPhoneNumber("a15-123-1235"))
print("Is jo mama a phone number?") # False
print(isPhoneNumber("jo mama"))
print("Is 4131123-1234 a phone number?") # False
print(isPhoneNumber("4131123-1234"))

# Additionally we can use the isPhoneNumber function to find the phone number within a string of text
message = "Call me at 123-123-1234, please!"

for i in range(len(message)):
    block = message[i:i+12]

    if isPhoneNumber(block):
        print("Phone number found! " + block)
