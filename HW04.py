
"""
Georgia Institute of Technology - CS1301
HW04 - Strings, indexing and lists
Matthew Kistner
"""

#########################################

"""
Function Name: fixTickets()
Parameters: ticketNumber (str)
Returns: fixedTicket (str)
"""
def fixTickets(ticketNumber):
    fixedTicket = ""
    for char in ticketNumber:
        if char.isupper():
            fixedTicket += char.lower()
        elif char.islower():
            fixedTicket += char.upper()
        else:
            fixedTicket += char
    return fixedTicket
    pass

#########################################

"""
Function Name: secret()
Parameters: message (str)
Returns: secret message (str)
"""
def secret(message):
    newmsg = ""
    for word in message.split():
        newmsg += " " + word[::-1]
    newmsg = newmsg[1::]
    return newmsg
    pass

#########################################

"""
Function Name: countTickets()
Parameters: aList (list)
Returns: total (int) or error message (str)
"""
def countTickets(aList):
    ticketCount = 0
    itemIndex = 0
    for item in aList:
        if type(item) == int:
            if item > 3:
                return "Sorry {}, but you can only get a maximum of three tickets per person.".format(aList[itemIndex-1])
            else:
                itemIndex += 1
                ticketCount += item
                continue
        else:
            itemIndex += 1
    return ticketCount
    pass

#########################################

"""
Function Name: fieldTripRoster()
Parameters: friendList (list)
Returns: nameList (list)
"""
def fieldTripRoster(friendList):
    nameList = []
    for item in friendList:
        for string in item:
            if string in nameList:
                continue
            if type(string) == str:
                nameList.append(string)
            else:
                continue
    nameList.sort()
    return nameList
    pass

#########################################

"""
Function Name: isSublist()
Parameters: myList (list), otherList (list)
Returns: True or False (bool)
"""
def isSublist(myList, otherList):
    newList = []
    for item in myList:
        if item in otherList:
            newList.append(item)
    return newList == otherList
pass
