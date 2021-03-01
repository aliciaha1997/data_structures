# ABOUT
# This program finds a pair of numbers within an array that matches a given sum
# Author: Alicia Ngoc Diep Ha

input = [8, 7, 2, 5, 3, 1]
sum = 10

for i in range(len(input)-1):
    for j in range(len(input)-1):
        if (input[i] + input[j] == sum):
            print("Pair at indexes " + str(i) + " and " + str(j))