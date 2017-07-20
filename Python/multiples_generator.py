#import random
#randNum = random.sample(range(10, 99, 5), 18)
from random import randint
multiplesList = []

#def findMultiple(randNum):
#    genRandNum()
#    if multiples == 0:
#        print(randNum)
#    else:
#        print(randNum)
#        print("is not a multiple of 5.")

for i in range(100):
    randNum = randint(10, 99)
    multiplesList.append(randNum)

for multiple in multiplesList:
    if multiple%5 == 0:
        print(multiple)
