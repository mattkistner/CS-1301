
"""
Georgia Institute of Technology - CS1301
HW03 - Loops and Iteration
Matthew Kistner
"""

#########################################

"""
Function Name: userReplace()
Parameters: startingString (str), username (str)
Returns: replacedString (string)
"""
def userReplace(startingString, username):
    replacedString = ""
    for c in startingString:
        if c != "$":
            replacedString += c
        elif c == "$":
            replacedString += username
    return replacedString
            
    pass

#########################################

"""
Function Name: specialChar()
Parameters: characterString (str)
Returns: sumOfIndices (int)
"""
def specialChar(characterString):
    count = 0
    sumOfIndices = 0
    specialCharacters = "!@#$%^&*."
    for c in characterString:
        if c not in specialCharacters:
            count += 1
        elif c in specialCharacters:
            sumOfIndices += count
            count += 1
    return sumOfIndices
        
    pass

#########################################

"""
Function Name: footballGame()
Parameters: score1 (str), score2 (str), team1 (str), team2 (str)
Returns: winningTeam (string)
"""
def footballGame(score1, score2, team1, team2):
    s1 = int(score1[0]) +  int(score1[2]) +  int(score1[4]) +  int(score1[6])
    s2 = int(score2[0]) + int(score2[2]) + int(score2[4]) + int(score2[6])
    if s1 > s2:
        return team1
    elif s2 >  s1:
        return team2
    elif s1 == s2:
        return "It's a tie!"
    pass

#########################################

"""
Function Name: buyTheDip()
Parameters: currentPrice (float), finalPrice (float), growth (float)
Returns: days (int)
"""
def buyTheDip(currentPrice, finalPrice, growth):
    days = 0
    while currentPrice > finalPrice:
        perday = currentPrice * (1 + growth / 100)
        currentPrice = perday
        days += 1
    return days
pass

#########################################

"""
Function Name: questionMaker()
Parameters: questions (str), subQuestions (str)
Returns: combinedQuestions (str)
"""
def questionMaker(questions, subQuestions):
    combinedQuestions = ""
    for a in questions:
        for c in subQuestions:
            combinedQuestions += a+c
    return combinedQuestions
pass
