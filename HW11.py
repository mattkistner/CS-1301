"""
Georgia Institute of Technology - CS1301
HW11
Matthew Kistner
"""

#########################################

"""
Function Name: potluck()
Parameters: food list (list)
Returns: food types (dict)
"""
def potluck(foodList):
    foodTypes = {}
    for food in foodList:
        if food[1] in foodTypes:
            foodTypes[food[1]].append(food[0])
        else:
            foodTypes[food[1]]  = [food[0]]
    return foodTypes
    pass

#########################################

"""
Function Name: insertEmoji()
Parameters: message (str), emojis (dict)
Returns: final message (str)
"""
def insertEmoji(message, emojiDict):
    finalMsg = ""
    for word in message.split():
        if "*" in word:
            for emoji in emojiDict:
                if emoji == word[1:]:
                    finalMsg += emojiDict[emoji] + " "
        else:
            finalMsg += word + " "
    return finalMsg[:-1]
    pass

    
#########################################

"""
Function Name: buyTickets()
Parameters: ticket prices (dict)
Returns: best website and time to buy (str)
"""
def buyTickets(ticketPrices):
    price = 1000
    for options in ticketPrices:
        for prices in ticketPrices[options]:
            if prices[1] < price:
                price = prices[1]
    for options in ticketPrices:
        for prices in ticketPrices[options]:
            if prices[1] == price:
                return "Buy tickets from {} at {}pm.".format(options, prices[0])

#########################################

"""
Function Name: dinnerLocation()
Parameters: preferred locations (dict), location (str)
Returns: whether majority of people favor that certain time (bool)
"""
def dinnerLocation(preferences, location):
    count = 0
    for locations in preferences:
        for places in preferences[locations]:
            if places == location:
                count += 1
    return count > (len(preferences)//2)
    pass

#########################################

"""
Function Name: sumNestedList()
Parameters: nested list (list)
Returns: sum of all integers (int)
"""
def sumNestedList(nestList):
    if nestList == []:
        return 0
    elif type(nestList[0]) == int:
        return nestList[0] + sumNestedList(nestList[1:])
    else:
        return sumNestedList(nestList[0]) + sumNestedList(nestList[1:])
    pass
