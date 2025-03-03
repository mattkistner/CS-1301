"""
Georgia Institute of Technology - CS1301
HW06 - Dictionaries and Try/Except
Matthew Kistner
"""

#########################################

"""
Function Name: possibleMovies()
Parameters: movies(dict), time (str)
Returns: list of movie names (list)
"""
def possibleMovies(movies, time):
    movieList = []
    for movie in movies:
        if time in movies[movie]:
            movieList.append(movie)
        else:
            continue
    return sorted(movieList)
    pass

#########################################

"""
Function Name: gameSelector()
Parameters: gameList (list), filterType (str)
Returns: dictionary of games mapped to a boolean value (dict)
"""
def gameSelector(gameList, filterType):
    gameDict = {}
    for game in gameList:
        if filterType == "even":
            if len(game) == 0:
                gameDict[game] = False
            elif len(game) % 2 == 0:
                gameDict[game] = True
            else:
                gameDict[game] = False
        elif filterType == "odd":
            if len(game) % 2 ==  0:
                gameDict[game] = False
            else:
                gameDict[game] = True
    return gameDict
    pass

    
#########################################

"""
Function Name: foodDecoder()
Parameters: secretList1 (list), secretList2 (list)
Returns: list of combined strings and the number of errors (list)
"""
def foodDecoder(secretList1, secretList2):
    decodedList = []
    i = 0
    errorCount = 0
    for item in secretList1:
        try:
            decodedList.append(item + secretList2[i])
            i += 1
        except:
            errorCount +=1
            i += 1
            continue
    decodedList.append(errorCount)
    return decodedList
    pass

#########################################

"""
Function Name: cheapestLocations()
Parameters: activities (dict)
Returns: dictionary mapping each activity to a location (dict)
"""
def cheapestLocations(activities):
    cheapDict = {}
    for activity in activities:
        tup4Sort = ()
        locations = activities[activity]
        if activities[activity] == {}:
            continue
        for location in locations:
            price = locations[location]
            tup4Sort += ((price, location),)
        cheapDict[activity] = sorted(tup4Sort)[0][1]
    return cheapDict 
    pass

#########################################

"""
Function Name: sportSuggestions()
Parameters: friends mapped to their suggested sports (dict)
Returns: dictionary mapping each sport to the list of friends who selected these sports (dict).
"""
def sportSuggestions(friends):
    suggestiveDict = {}
    for sports in friends.values():
        for sport in sports:
            sportList = []
            if sport in suggestiveDict:
                continue
            else:
                for person in friends:
                    if sport in friends[person]:
                        sportList.append(person)
                    else:
                        continue
                suggestiveDict[sport] = sorted(sportList)
    return suggestiveDict
    pass
