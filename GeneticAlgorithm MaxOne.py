import random
import copy


# Configuration
crossoverRate = 0.8
mutationRate = 0.1
populationSize = 6
bitSize = 10
improvementRequest = 2.0


# Create a new random candidate with the given size
def candidateCreation(size):
    output = []
    for i in range(size):
        output.append(random.randrange(0, 2))
    return output


# Selects 2 candidates
def select(population):
    selection = []
    for i in range(2):
        cumulativeProbabiltyList = cumSummationToCumProbabilityList(
            getCumSummation(population))
        pickedElement = rouletteSelect(cumulativeProbabiltyList, population)
        selection.append(pickedElement)
        population.remove(pickedElement)
    return selection


# Method that gives cumulative Summation of bitlist
def getCumSummation(population):
    sumCumList = []  # Sums of each bitlist
    for i in range(len(population)):
        if(i > 0):
            # Adds previous element to make list cumalative
            sumCumList.append(sum(population[i])+sumCumList[i-1])
        else:
            sumCumList.append(sum(population[i]))
    return sumCumList


# Method that makes cumSummationList into probability list
# Problem is if list is null then gets terminated
def cumSummationToCumProbabilityList(sumCumList):
    total = sumCumList[-1]
    for i in range(len(sumCumList)):
        sumCumList[i] = sumCumList[i] / total
    return sumCumList


# Selects by roulette selection
def rouletteSelect(cumProbList, population):
    pick = random.random()
    cumProbList.insert(0, 0)
    for i in range(len(cumProbList)):
        if(i > 0 and pick >= cumProbList[i-1] and pick <= cumProbList[i]):
            return population[i-2]


# Makes use of single point crossover
def crossOver(selectedParents):
    tempList = copy.deepcopy(selectedParents)
    if(random.random() <= crossoverRate):
        selectedParents[0][bitSize//2:bitSize] = selectedParents[1][bitSize//2:bitSize]
        selectedParents[1][bitSize//2:bitSize] = tempList[0][bitSize//2:bitSize]
    return selectedParents


# Mutate the bits with a low probability
def mutate(bitList):
    for i in range(len(bitList)):
        if(random.random() <= mutationRate):
            bitList[i] = bitSwitch(bitList[i])
    return bitList


# Switches the bit on/off
def bitSwitch(bit):
    if(bit == 1):
        bit = 0
    elif(bit == 0):
        bit = 1
    return bit


def result(population):
    resultInfo = []
    for i in range(len(population)):
        resultInfo.append(sum(population[i]))
    return sum(resultInfo)/len(resultInfo)


def main():
    population = []
    numberIterations = 0
    for i in range(populationSize):
        population.append(candidateCreation(bitSize))
    meanInit = result(population)
    print("Mean of init population: " + str(meanInit))
    while True:
        selectedParents = select(population)
        selectedChildren = crossOver(selectedParents)
        selectedChildren[0] = mutate(selectedChildren[0])
        selectedChildren[1] = mutate(selectedChildren[1])
        population.append(selectedChildren[0])
        population.append(selectedChildren[1])
        if(result(population) > meanInit*improvementRequest):
            print("After "+str(numberIterations)+" iterations")
            print("Mean of new population: " + str(result(population)))
            break
        else:
            numberIterations = numberIterations + 1


if __name__ == "__main__":
    main()
