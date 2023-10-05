###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #

import csv
from statistics import mean as mean

#open with covid csv file
countriesDictionary={}

#we read csv into before data structure
with open('./covid.csv') as file:
    fileReader=csv.reader(file)
    for row in fileReader:
        try:
            #ignore first row of metrics
            if row[0] == "Country":
                continue
            #row is country, confirmed, death,recovered,active: we pick important value
            #we pick in paris of country : [confirmed,death,active]
            covidValueList = [row[1],row[2],row[4]]
            countriesDictionary[row[0]] = covidValueList

        #catch error when file reading problem ocurred
        except Exception as err:
            print(Exception) 

#print and check the covid infection result
print("country, confirmed, death,active")
for country in countriesDictionary.items():
    print(country)

#categories container
covidDictionary5000={}
covidDictionary1000={}
covidDictionary500={}

#create 5000,1000,500 countries dictionary.
#our item data structure of dictionary is countryName : [confirmed, death, active]
for country, covidValueList in countriesDictionary.items():
    if int(covidValueList[2])>5000:
        covidDictionary5000[country] = covidValueList
    elif int(covidValueList[2])>1000:
        covidDictionary1000[country] = covidValueList
    elif int(covidValueList[2])>500:
        covidDictionary500[country] = covidValueList

# resuable death rate caculator death/confirmed
def meanDeathRateCalculator(covidDictionary):
    sumDeathRate = 0
    #iterate to sum total death rate
    for covidValueList in covidDictionary.values():
        tempDeathRate = int(covidValueList[1]) / int(covidValueList[0])
        sumDeathRate += tempDeathRate
    #by divided country total number we obtain total death rate, sum(death rate)/countries Number
    meanDeathRate = sumDeathRate / len(covidDictionary)*100
    return meanDeathRate

#print results
meanDeathRate5000 = meanDeathRateCalculator(covidDictionary5000)
print(f"size in 5000 countries mean death rate: {meanDeathRate5000}%")
meanDeathRate1000 = meanDeathRateCalculator(covidDictionary1000)
print(f"size in 1000 countries mean death rate: {meanDeathRate1000}%")
meanDeathRate500 = meanDeathRateCalculator(covidDictionary500)
print(f"size in 500 countries mean death rate: {meanDeathRate500}%")
