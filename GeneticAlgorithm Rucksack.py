import random
import copy


# Configuration of Rucksack problem
totalItem = 15  # Optionally takes 15 items


# Gets a random item based on amount
def itemCreation(amount):
    output = []
    for i in range(amount):
        output.append(random.expovariate(0.1))
    return output


def main():
    items = itemCreation(totalItem)
    print(items)

if __name__ == "__main__":
    main()
