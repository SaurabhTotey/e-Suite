"""
Made by Saurabh Totey

A program to see the average number of random numbers it takes to get to 1
Based on the reddit comment
https://www.reddit.com/r/AskReddit/comments/6il1jx/whats_the_coolest_mathematical_fact_you_know_of/dj78wzt/
"""


import sys
import random
import math


# How many runs to test
totalNumRuns = sys.maxsize
# A list of the number of random numbers it took to get to 1
amtOfNumsToGetOne = []

# A loop that actually figures out how many random numbers it has taken to get to 1 and displays the current number of
# needed random numbers and the average number of needed random numbers up until that point
for counter in range(totalNumRuns):
    currentTotal = 0
    currentNumRuns = 0
    while currentTotal < 1:
        currentTotal += random.random()
        currentNumRuns += 1
    amtOfNumsToGetOne.append(currentNumRuns)
    averageNumOfRandNumsToOne = sum(amtOfNumsToGetOne) / float(len(amtOfNumsToGetOne))
    # Prints the results so the user can see the current stats
    print("Iteration:                                            ", counter)
    print("Number of needed random numbers to get to one:        ", currentNumRuns)
    print("Average number of needed random numbers to get to one:", averageNumOfRandNumsToOne)
    print("Difference of average from e:                         ", math.fabs(math.e - averageNumOfRandNumsToOne))
    print("\n")
