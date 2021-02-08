# A file for various dice rolling functions

def sum_of_dice(number_of_sides, number_of_dice):
    """  return a total roll of a bunch of dice
    specify the number of sides of the dice (all the same)
    specify the number of dice

    return the total of rolling all those dice
    """

    import random
    sumOfRoll = 0

    for die in range(number_of_dice):
        sumOfRoll += random.randint(1, number_of_sides)

    return sumOfRoll

