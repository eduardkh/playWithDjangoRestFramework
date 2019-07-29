myString = "heLL world"
inMyString = "hello"
if inMyString in myString.lower():
    print(f"yes '{inMyString}' is in the string")
elif myString == "":
    print(f"the string is empty")
else:
    print(f"no '{inMyString}' is NOT in the string")