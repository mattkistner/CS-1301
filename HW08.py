
"""
Georgia Institute of Technology - CS1301
HW08 -  API
Matthew Kistner
"""
import requests
#########################################

"""
Function Name: averagePopulation()
Parameters: regionalBloc(str)
Returns: average population(float)
"""
def averagePopulation(regionalBloc):
    baseURL = "https://restcountries.com/v2/regionalbloc/"
    data = requests.get(baseURL + regionalBloc)
    popData = data.json()
    regionalPop = 0
    countryCounter = 0
    for country in popData:
        regionalPop += country['population']
        countryCounter += 1
    avgPop = round((regionalPop/countryCounter), 2)
    return avgPop
    pass

#########################################

"""
Function Name: commonCountries()
Parameters: langTup1(tuple), langTup2(tuple)
Returns: list of countries(list)
"""
def commonCountries(langTup1, langTup2):
    baseURL = "https://restcountries.com/v2/lang/"
    langIdata = requests.get(baseURL + langTup1[0])
    lang1data = langIdata.json()
    langIIdata = requests.get(baseURL + langTup2[0])
    lang2data = langIIdata.json()
    countryList = []
    langList = []
    for countries in lang1data:
        countryList.append(countries["name"])
    for countries in lang2data:
        if countries["name"]  in countryList:
            langList.append(countries["name"])
    langList.sort()
    return langList
    pass

#########################################

"""
Function Name: uniqueRegions()
Parameters: countryList(list)
Returns: True or False(bool) or Error Message(str)
"""
def uniqueRegions(countryList):
    baseURL = "https://restcountries.com/v2/alpha?codes="
    datastr = ""
    for code in countryList:
        datastr += code + ","
    regionData = requests.get(baseURL + datastr)
    sameRegionData = regionData.json()
    count = 0
    for countries in sameRegionData:
        try:
            if count == 0:
                region = str(countries["region"])
                count += 1
            elif countries["region"] == region:
                continue
            else:
                return True
        except:
            return "Invalid country code!"
    return False
   
    pass

#########################################

"""
Function Name: organizeCapitals()
Parameters: capitalList(list)
Returns: Dictionary mapping regions to a list of countries(dict)
"""
def organizeCapitals(capitalList):
    capitalDict = {}
    baseURL = "https://restcountries.com/v2/capital/"
    for capital in capitalList:
        data = requests.get(baseURL + str(capital))
        countryData = data.json()
        for country in countryData:
            try:
                if country["region"] in capitalDict:
                    capitalDict[country["region"]].append(country["name"])
                else:
                    capitalDict[country["region"]] = [country["name"]]
            except:
                continue
    return capitalDict
    pass

#########################################

"""
Function Name: visitableCountries()
Parameters: countryCodeList(list)
Returns: list of country names(list)
"""
def visitableCountries(countryCodeList):
    borderList = []
    baseURL = "https://restcountries.com/v2/alpha?codes="
    datastr = ""
    for code in countryCodeList:
        datastr += str(code) + ","
    countryData = requests.get(baseURL + datastr)
    borderData = countryData.json()
    i = 0
    for country in borderData:
        if i == 0:
            borderList.append(country["name"])
            i += 1
        elif i >= 1 and countryCodeList[i-1] in country["borders"]:
            i += 1
            borderList.append(country["name"])
        elif i >= (len(countryCodeList)-1):
            continue    
        elif countryCodeList[i+1] in country["borders"]:
            i += 1
            borderList.append(country["name"])
    return borderList
            
    pass
