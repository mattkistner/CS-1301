"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Expressions
Matthew Kistner
"""

#########################################

"""
Function Name: clubPoints()
Parameters: N/A
Returns: None
"""
def clubPoints():
    clubsjoined =int(input("How many clubs have you joined? "))
    clubfriends = int(input("How many friends have you gotten to join clubs? "))
    result = str((clubsjoined*30)+(clubfriends*50))
    print("You have won a total of {} points!!".format(result))

#########################################

"""
Function Name: moveIn()
Parameters: N/A
Returns: None
"""
def moveIn():
    freshmen =int(input("How many freshman do you plan to assist? "))
    sophomores = int(input("How many sophomores do you plan to assist? "))
    juniors = int(input("How many juniors do you plan to assist? "))
    total_min = ((freshmen*35)+(sophomores*20)+ (juniors*15))
    hours = (total_min // 60)
    minutes = (total_min % 60)
    students = (freshmen+sophomores+juniors)
    print("It will take {} hours and {} minutes to help {} students with move-in today.".format(hours,minutes,students))

#########################################

"""
Function Name: tireArea()
Parameters: N/A
Returns: None
"""
def tireArea():
    r = float(input("What is the radius of the tire? "))
    pi = 3.14
    area = round((pi *( r ** 2)), 2)
    print("The area of the tire is {}.".format(area))

#########################################

"""
Function Name: dining()
Parameters: N/A
Returns: None
"""
def dining():
    panda_ex = int(input("How many meals do you want to order from Panda Express? "))
    rising_roll = int (input("How many meals do you want to order from Rising Roll? "))
    cfa = int(input("How many meals do you want to order from Chick-fil-A? "))
    tip = int(input("What percent would you like to tip? "))
    paid = round(((panda_ex * 6)+(rising_roll*8)+(cfa*9)),2)
    tip2 = round((paid * (tip/100)),2)
    paid2 = round((((panda_ex * 6)+(rising_roll*8)+(cfa*9))+tip2),2)
    print("You paid ${} and tipped ${}.".format(paid2,tip2))

#########################################

"""
Function Name: weeklyBudget()
Parameters: N/A
Returns: None
"""
def weeklyBudget():
    budg = float(input("How much is your budget this week? "))
    save = float(input("What percentage do you want to save? "))
    save_ = (100-save)/100
    total = float((budg*save_) - 34.90)
    print("You have ${} left after savings and fees.".format(total))
