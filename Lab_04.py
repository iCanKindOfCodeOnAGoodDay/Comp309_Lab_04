"""
    Scott Quashen
    CSC 309 SFSU Spring 2024
    Lab #4
    Created on Tuesday Feb 20 22:30 2024  

    Description: 
        The program uses a random number function to create a list of numbers.
        That same list is then created using list comprehension, and manipulated.
        
    
    Inputs: 
        S: int (seed value)
        N: int (amount of items in L)
        Min, Max: int values for creating random number range

    Returns: 
        L: List of random numbers

    Dependencies: Random

    Assumptions: developed and tested using Spyder 5.4.3, Python version 3.11.5 on macOS 14.3.1
"""

#--------------------------project imports section

import random




#--------------------------function definitions section

def randomNumbers(size, seed, min, max):
    """
    
    Description
    ----------
    randomNumbers() returns a list of size N containing pseudo-random numbers based on seed value

    Parameters
    ----------
    size : 
        int
        Amount of random numbers to create and add to our list
    seed : 
        int
        Used for creating the same random numbers each time program is run
    min : 
        int
        Minimum value that a random number could be
    max : 
        int
        Maximum value that a random number could be

    Returns
    -------
    L : 
        List
        Contains the random integers  

    """
    
    L = []
    random.seed(seed, int)
    for i in range(N):
        L.append(random.randint(min, max))
    return L

# end of randomNumbers() function




#--------------------------main code section

# Set list size
N = 21

# Set seed size
S = 22

# Create list L1 size N with a for loop and fill with random numbers in range [-99, 99] with S seed value
L1 = randomNumbers(N, S, -99, 99)
print("L1 = " + str(L1))

# L2: Build the same list L1 but using an List Comprehension
L2 = [t for t in randomNumbers(N, 22, -99, 99)]
print("L2 = " + str(L2))

# L3: subset of L2 that is >= 0
L3 = [t for t in L2 if t >= 0]
print("L3 = " + str(L3))

# L4: subset of L2 that are even numbers >= 0
L4 = [t for t in L2 if t >= 0 and t % 2 == 0]
print("L4 = " + str(L4))

# L5: subset of L2 that are odd numbers > 0
L5 = [t for t in L2 if t > 0 and t % 2 != 0]
print("L5 = " + str(L5))




