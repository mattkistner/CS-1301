"""
Georgia Institute of Technology - CS1301
HW07 -  File I/O & CSV
Matthew Kistner
"""

#########################################

"""
Function Name: sortByArtist()
Parameters: filename (str), artist (str)
Returns: list of songs (list)
"""
def sortByArtist(filename, artist):
    playlist = []
    musicFile = open(filename, "r")
    count=0
    songInfoTup = ()
    for info in musicFile.readlines()[1:]:
        songInfoTup += (info,)
        count+=1
        if count == 4:
            count = 0
            playlist.append(songInfoTup)
            songInfoTup = ()
    musicFile.close()
    finalPlaylist = []
    for void, song, genre, musician in playlist:
        if musician[:-1] == artist:
            finalPlaylist.append(song[:-1])
        elif musician == artist:
            finalPlaylist.append(song[:-1])
    return finalPlaylist
    pass

#########################################

"""
Function Name: genreFilter()
Parameters: filename (str)
Returns: mapping of songs to lists of genres of that song (dict)
"""
def genreFilter(filename):
    playlist = []
    musicFile = open(filename, "r")
    count=0
    songInfoTup = ()
    for info in musicFile.readlines()[1:]:
        songInfoTup += (info,)
        count+=1
        if count == 4:
            count = 0
            playlist.append(songInfoTup)
            songInfoTup = ()
    musicFile.close()
    genreDict = {}
    for void, song, genre, artist in playlist:
        if genre[:-1] in genreDict:
            genreDict[genre[:-1]].append(song[:-1])
        else:
            genreDict[genre[:-1]] = [song[:-1]]
    return genreDict
    pass

#########################################

"""
Function Name: sortByGenre()
Parameters: filename (str), genre (str), output filename (str)
Returns: None (NoneType)
"""
def sortByGenre(filename, genre, outputFile):
    playlist = []
    musicFile = open(filename, "r")
    count=0
    songInfoTup = ()
    for info in musicFile.readlines()[1:]:
        songInfoTup += (info,)
        count+=1
        if count == 4:
            count = 0
            playlist.append(songInfoTup)
            songInfoTup = ()
    musicFile.close()
    genreDict = {}
    for void, song, typ, artist in playlist:
        if typ[:-1] in genreDict:
            genreDict[typ[:-1]].append(song[:-1] + ' - ' + artist)
        elif typ[:-1] not in genreDict:
            genreDict[typ[:-1]] = [song[:-1] + ' - ' + artist]
    for key in genreDict:
        genreDict[key].sort()
    genreFile = open(outputFile, "w")
    genreFile.write(genre + "\n")
    count = 1
    if genre not in genreDict:
        genreFile.close()
    else:
        genreFile.write("\n")
        for value in genreDict[genre]:
            if value == genreDict[genre][-1]:
                genreFile.write(str(count) + ". " + value[:-1])
                count += 1
            elif "\n" not in value:
                genreFile.write(str(count) + ". " + value + "\n")
                count += 1
            else:
                genreFile.write(str(count) + ". " + value)
                count += 1
        genreFile.close()
    pass

#########################################

"""
Function Name: biggestSuccess()
Parameters: filename (str), artists (list)
Returns: artist and percentage (tuple)
"""
def biggestSuccess(filename, artistList):
    artistFile = open(filename, "r")
    artistFile.readline()
    statistics = artistFile.readlines()
    artistFile.close()
    artistTupleList = []
    if artistList == []:
        return ()
    for value in statistics:
        usefulList = value.split(",")
        if usefulList[0] in artistList:
            try:
                if "\n" not in usefulList[3]:
                    ratio = int(usefulList[3]) / int(usefulList[1])
                else:
                    ratio = int(usefulList[3][:-1]) / int(usefulList[1])
            except:
                ratio = 0
            artistTupleList.append((ratio*100, usefulList[0]))
    artistTupleList.sort()
    if artistTupleList[-1][0] == 0:
        return ()
    else:
        return (artistTupleList[-1][1], round(artistTupleList[-1][0], 2))
    pass

#########################################

"""
Function Name: grammyAwards()
Parameters: filename (str), artists (list)
Returns: category of artists by celebrity status (dict)
"""
def grammyAwards(filename, artistList):
    artistFile = open(filename, "r")
    artistFile.readline()
    information = artistFile.readlines()
    artistFile.close()
    grammyDict = {'A-List': [], 'B-List': [], 'C-List': []}
    for value in information:
        artistfacts = value.split(",")
        if artistfacts[0] in artistList:
            try:
                if "\n" not in artistfacts[3]:
                    percent = (int(artistfacts[3])/int(artistfacts[1]))*100
                else:
                    percent = (int(artistfacts[3][:-1])/int(artistfacts[1]))*100
            except:
                percent = 0
                continue
            if percent <= 30:
                grammyDict['C-List'].append(artistfacts[0])
            elif percent > 30 and percent <= 70:
                grammyDict['B-List'].append(artistfacts[0])
            else:
                grammyDict['A-List'].append(artistfacts[0])
    return grammyDict
    pass
