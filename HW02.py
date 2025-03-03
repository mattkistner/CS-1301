"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
Matthew Kistner
"""

#########################################

"""
Function Name: intramuralGames()
Parameters: gameName (str), numFriends (int)
Returns: None (NoneType)
"""
def intramuralGames(gameName, numFriends):
    if numFriends < 2:
        print( "Let's choose something else.")
    elif numFriends>=2 and numFriends<6:
        print ("We will try out {} for a little bit!".format(gameName))
    else:
        print("Let's register for {}!!!" .format(gameName))
    pass

#########################################

"""
Function Name: goShopping()
Parameters: item (str), quantity (int), budget (float)
Returns: moneyLeft (float) or error message (str)
"""
def goShopping(item, quantity, budget):
    if item == "Shorts":
        price = 13.00
    elif item == "T-Shirts and Tanks":
        price = 9.75
    elif item == "Swimwear":
        price = 20.00
    elif item == "Sunglasses":
        price = 7.50
    else:
        price = 15.50
    price_ = float(quantity) * price
    if price_ > budget:
        return "Not enough money!"
    else:
        return float(budget - price_)
    pass

#########################################

"""
Function Name: getDinner()
Parameters: budget (float), diningOption (str)
Returns: restaurantName (str)
"""
def getDinner(budget, diningOption):
    if budget <= 10.00:
        if diningOption == "Takeout" or diningOption ==  "Delivery":
            return "Chick Fil A"
        elif diningOption == "Indoor" or diningOption == "Outdoor":
            return "Moe's"
    elif budget > 10.00 and budget <= 20.00:
        if diningOption == "Indoor" or diningOption == "Takeout":
            return "Tin Drum"
        elif diningOption == "Outdoor" or diningOption == "Delivery":
            return "Umma's"
    elif budget > 20.00 and budget <= 30.00:
        if diningOption == "Indoor" or  diningOption == "Outdoor" or diningOption == "Takeout":
            return "Yeah Burger"
        elif diningOption == "Delivery":
            return "Flip Burger"
    elif budget > 30.00 and budget <= 40.00:
        if diningOption == "Indoor":
            return "Two Urban Licks"
        elif diningOption == "Takeout" or diningOption == "Delivery" or diningOption == "Outdoor":
            return "Gypsy Kitchen"   
    pass

#########################################

"""
Function Name: backupRestaurant()
Parameters: budget (float), diningOption (str), backup (str)
Returns: decision (str)
"""
def backupRestaurant(budget, diningOption, backup):
    firstchoice = getDinner(budget, diningOption)
    if firstchoice == "Chick Fil A" or firstchoice == "Umma's" or firstchoice == "Gypsy Kitchen" or firstchoice == "Flip Burger":
        time = 15
    else:
        time = 45
    if backup == "Chick Fil A" or backup == "Umma's" or backup == "Gypsy Kitchen" or backup == "Flip Burger":
        time_ = 15
    else:
        time_ = 45
    if time <= time_ :
        return "Yay, you can get dinner at your first choice, {}.".format(firstchoice)
    else:
        return "You'll have to get dinner at {} instead.".format(backup)
    pass

#########################################

"""
Function Name: rideShare()
Parameters: number of riders (int), miles(int), rideShareOptionaA (str), rideShareOptionaB (str)
Returns: rideShareOption (str)
"""
def rideShare(numRiders, miles, rideShareOptionaA, rideShareOptionaB):
    if rideShareOptionaA == "Uber":
        if numRiders > 3:
            cost = 5.50 * miles
        else:
            cost = 5 + (5.50 * miles)
    elif rideShareOptionaA == "Lyft":
        cost = 10 + (1.50 *miles)
    elif rideShareOptionaA == "Hitch":
        if numRiders > 2:
            cost = (7.50 * miles) - (10 * numRiders)
        else:
            cost = 7.50 * miles
    elif rideShareOptionaA == "Taxi":
        cost = 18 * miles
    if rideShareOptionaB == "Uber":
        if numRiders > 3:
            cost_ = 5.50 * miles
        else:
            cost_ = 5 + (5.50*miles)
    if rideShareOptionaB == "Lyft":
        cost_ = 10 + (1.50 *miles)
    elif rideShareOptionaB == "Hitch":
        if numRiders > 2:
            cost_ = (7.50 * miles) - (10 * numRiders)
        else:
            cost_ = 7.50 * miles
    elif rideShareOptionaB == "Taxi":
        cost_ = 18 * miles
    if cost <= cost_:
        return rideShareOptionaA
    else:
        return rideShareOptionaB
    pass
