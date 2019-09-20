#Objective 
#In this challenge, we're going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.
#Task 
#Given an integer, , print its first  multiples. Each multiple  (where ) should be printed on a new line in the form: n x i = result.
 
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

for i in range(1, 11):
    print(str(n) + " x " + str(i) + " = ", end='')
    print(i*n)
