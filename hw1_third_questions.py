# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country
def total_registered_cases(registeredCountries, countryName):
    totalCasesCounter = 0
    for cName,cCases in registeredCountries.items():
        if countryName == cName:
            for nInfected in cCases:
                totalCasesCounter+=nInfected
    return totalCasesCounter

countries = {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],'Italy': [6, 8, 1, 7]}
testCountry1='Spain'
cases=total_registered_cases(countries,testCountry1)
print("\nEx7")
print(testCountry1,"have total registered cases:",cases)
# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#

def total_registered_cases_per_country(registeredCountries):
    countryTotalCasesDict = {}

    for c in registeredCountries:
        totalRegisteredCases = total_registered_cases(countries, c)
        countryTotalCasesDict[c] = totalRegisteredCases

    return countryTotalCasesDict


dictCountryResult = total_registered_cases_per_country(countries)
print("\nEx8")
print("dictionary:",dictCountryResult)

# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases

def country_with_most_cases(registeredCountries):
    resultDict = {}
    maxTotalCasesCounter = 0

    for countryName in list(registeredCountries.keys()):
        currentCountryCasesAmountCounter = total_registered_cases(registeredCountries,countryName)
        
        maxDict = {}
        if currentCountryCasesAmountCounter > maxTotalCasesCounter:
            tempDict={}
            maxTotalCasesCounter = currentCountryCasesAmountCounter
            tempDict[countryName] = maxTotalCasesCounter
            maxDict = tempDict
        resultDict = maxDict
    return resultDict

testMaximumTotalCases = country_with_most_cases(countries)
print("\nEx9")
print("maximum total value is: ", testMaximumTotalCases)



###############
