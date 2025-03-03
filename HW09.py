"""
Georgia Institute of Technology - CS1301
HW09 - Recursion
Matthew Kistner
"""

#########################################

"""
Function Name: add()
Parameters: list of ints (list)
Returns: total (int)
"""
def add(intList):
    if intList == []:
        return 0
    else:
        return int(intList[0]) + add(intList[1:])
    pass

#########################################

"""
Function Name: decoder()
Parameters: encryption (str)
Returns: codeword (str)
"""
def decoder(encryption):
    if encryption == '':
        return ''
    else:
        if encryption[0].isalpha():
            return encryption[0] + decoder(encryption[1:])
        else:
            return decoder(encryption[1:])
    pass

    
#########################################

"""
Function Name: pirateTreasure()
Parameters: directions (list)
Returns: distance_to_treasure (int)
"""
def pirateTreasure(directionList):
    if directionList == []:
        return 0
    else:
        if directionList[0] == 'up':
            return 1 + pirateTreasure(directionList[1:])
        elif directionList[0] == 'down':
            return -1 + pirateTreasure(directionList[1:])
        else:
            pass
    pass

#########################################

"""
Function Name: lengthDict()
Parameters: list of names (list)
Returns: dictionary mapping names to length (dict)
"""
def lengthDict(nameList):
    if len(nameList) == 0:
        return {}
    else:
        conDict = lengthDict(nameList[:-1])
        conCount = 0
        for letter in nameList[-1]:
            if letter.lower() not in "aeiou":
                conCount += 1
        conDict[nameList[-1]] = conCount
        return conDict
    pass

#########################################

"""
Function Name: balancedStr()
Parameters: string of characters (str)
Returns: isBalanced (bool)
"""
def balancedStr(charStr):
    if charStr == "":
        return True
    else:
        if charStr[0].isupper() and charStr[-1].isupper():
            return balancedStr(charStr[1:-1])
        elif charStr[0].islower() and charStr[-1].islower():
            return balancedStr(charStr[1:-1])
        elif len(charStr) == 1:
            return True
        else:
            return False
    pass
