"""
Georgia Institute of Technology - CS1301
HW05 - Lists, Tuples, and Modules
Matthew Kistner
"""

#########################################

"""
Function Name: dinnerParty()
Parameters: list of names and availabilities (list), day (str)
Returns: list of friends (list)
"""
def dinnerParty(availabilities, day):
    friends = []
    for (name, days) in availabilities:
        if day in days:
            friends.append(name)
        else:
            continue
    return friends
    pass

#########################################

"""
Function Name: whatShouldIWear()
Parameters: list of temperatures (list), list of recommendations (list)
Returns: list of tuples (list)
"""
def whatShouldIWear(temps, recs):
    index = 0
    finalList = []
    while index < len(temps):
        finalList.append((temps[index], recs[index]))
        index += 1
    return finalList
    pass

    
#########################################

"""
Function Name: cheapMeals()
Parameters: list of strings (list) and budget (float)
Returns: tuple containing menu items (tuple)
"""
def cheapMeals(menu, budget):
    affordableList = []
    affordableFood = ()
    for item in menu:
        itemRef = item.split(" - $")
        if float(itemRef[1]) <= budget:
            affordableList += (itemRef[1], itemRef[0],),
        else:
            continue
    for item in sorted(affordableList):
        affordableFood += (item[1],)
    return affordableFood
    pass

#########################################

"""
Function Name: wednesdays()
Parameters: list of tuples with dates and holidays (list)
Returns: list of holidays (list)
"""
def wednesdays(holidays):
    import calendar
    wednesdayList = []
    for day in holidays:
        (holiday, day, month, year) = day
        if calendar.weekday(year, month, day) == 2:
            wednesdayList.append(holiday)
    return wednesdayList
    pass

#########################################

"""
Function Name: starbucksFanatic()
Parameters: list of starbucks menu items (list)
Returns: list of tuples containing menu item name and price (list)
"""
def starbucksFanatic(fallMenuItems):
    import starbucks
    itemList = []
    total = 0
    for item in fallMenuItems:
        if starbucks.menu(item) == 0:
            continue
        else:
            itemList.append((item, starbucks.menu(item)),)
    for item in itemList:
        total += float(item[1])
    itemList.append(round(total,2))
    return itemList
    pass

