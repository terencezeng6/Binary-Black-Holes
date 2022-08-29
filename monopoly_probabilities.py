#Ok so this is a little bit of code I just wrote for fun - it calculates the probabilities that you will land on a certain square, and not pass through it.
#Landing on a square may take several turns, and I used dynamic programming.

#Dynamic programming is essentially recursion - the difference is that the results are stored in some sort of data structure.
#This is so that when you run a function with the same parameters over and over again, the results don't have to be recalculated.

#For example, let's say you are 5 spaces from Boardwalk. Someone else owns Boardwalk, so you really don't want to land on it.
#The probability that you land on Boardwalk in one turn is 1/9, which is just basic math.
#However, you can also land on Boardwalk in 2 rolls - you can roll a 3 then a 2, or a 2 then a 3.
#The probability of these happening is 1/36 * 1/18 + 1/18 + 1/36 = 1/324. Not likely, but still something to consider!
#In this way, calculations are made for each position on the board from 1 square away to 39 squares away (there are 40 squares on a board).

#Drawbacks: This code does not account for squares such as chance, which can teleport you to different places.

import matplotlib.pyplot as plt #I used matplotlib to plot the data.

tests = 39 #number of squares, not including the target

chances = [0, 0] + ["." for i in range(tests-1)]
#dice[i] = chance that a pair of dice rolls the value i.
dice = [0, 0, 1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

#main dynamic programming function
def dp(x):
    if chances[x] != ".":
        return chances[x]
    res = dice[x] if x <= 12 else 0
    for i in range(2, min(12, x)):
        res += dice[i] * dp(x-i)
    chances[x] = res
    return res

#run the function (my code isn't set up great, so I have to run the function twice
dp(tests)
dp(tests-1)

#prints whole list for debugging
#for i in range(tests):
    #print("Distance from square = ", i, ": ", round(chances[i], 4) , "% chance of landing")

#make plot
a = [x for x in range(len(chances))]
plt.plot(a, chances)
plt.show()

#Conclusion: TBA

#Aside: one time I was playing with my family and owned the light blue monopoly of hotels on Oriental, Vermont, and Connecticut.
#To my surprise, the other 3 members passed by my hotels. This happened 3 times! 
#In my frustration, I coded this program and decided that I was extremely unlucky - the probability that this happens is about ______!
