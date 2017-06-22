"""
Made by Saurabh Totey

A program that finds e as a fraction
Based on a previous project
https://github.com/SaurabhTotey/Old-Python-Projects/blob/master/e%20in%20fraction%20form%20-%203.py
"""


import math


# Variables for the numerator and the denominator of the fraction form of e
numerator = 0
denominator = 0
# The number of iterations the program should go to to find e as a fraction: default is 171 because that is the largest
# value that the script can handle
maxRunNum = 171


for iteration in range(maxRunNum):
    # Calculates the new numerator and denominator for e as a fraction
    denominator = math.factorial(iteration)
    numerator = (numerator * iteration) + 1
    # Makes a simplified numerator and denominator for representing e as a fraction
    GCD = math.gcd(numerator, denominator)
    simpleNumerator = int(numerator / GCD)
    simpleDenominator = int(denominator / GCD)
    # Calculates the necessary information about the fraction form of e
    obtained_e = simpleNumerator / float(simpleDenominator)
    # Prints the results so the user can see the current stats
    print("Iteration " + str(iteration) + "'s e = " + str(obtained_e))
    print("Difference with e:", math.e - obtained_e)
    print("")
    print(simpleNumerator)
    print("-" * len(str(simpleNumerator)))
    print(simpleDenominator)
    print("\n\n")
