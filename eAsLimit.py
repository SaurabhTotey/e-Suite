"""
Made by Saurabh Totey
"""


import sys
import math


# How many runs to test
totalNumRuns = sys.maxsize


# This loops through and performs the calculation of the limit version of e with increasing limit values
for iteration in range(1, totalNumRuns):
    obtained_e = (1 + 1 / float(iteration)) ** iteration
    # Prints the results so the user can see the current stats
    print("Iteration:        ", iteration)
    print("Obtained e:       ", obtained_e)
    print("Difference with e:", math.e - obtained_e)
    print("\n")
