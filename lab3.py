years = int(input("Enter the number of years: "))

## part 1 - calculate population given number of years
def calculatePopulation():
    population = 89.2
    counter = 0
    # if moving forward in time, multiply by 1.023 for each year that passes and add 1 to the counter of years passed
    # repeat the multiplication and add to the counter until the counter matches the number of years passed
    if years >= 0:
        while counter < years:
            population = population * 1.023
            counter+=1
    # if moving backwards in time, divide by 1.023 for each year going back and subtract 1 from the counter of years
    # repeat the division and subtract from counter until the counter matches the number of years
    else:
        while counter > years:
            population = population/1.023
            counter-=1
    return population

print("The population of Mexico in " + str(1990 + years) + " is " + str(calculatePopulation()) + " million")

## part 2 - given the population, find the year
origPopulation = int(input("enter population: "))

# given a population, find the year and return both the year it would have been and its calculated population
def calculateYear():
    population = 89.2
    year = 1990
    # if the given population is less than 89.2:
    # move backwards in time by dividing by 1.023 and subtract 1 from year with each year gone back
    if origPopulation < 89.2:
        while (population > origPopulation):
            population = population/1.023
            year-=1
    # if the given population is >= 89.2:
    # move forwards in time by multiplying by 1.023 and add 1 to the year for each year passed
    else:
        while (population < origPopulation):
            population *= 1.023
            year+=1
    return year, population

calculatedYear = calculateYear()
print("The population of Mexico in " + str(calculatedYear[0]) + " is " + str(calculatedYear[1]) + " million")
