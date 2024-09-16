import random

myList = []
userNum = int(input("How many numbers do you want the numbers do you want the list to contain: "))
for num in range(0, userNum):
    randInt = random.randint(0, 101)
    myList.append(randInt)

def sumList():
    print(myList)
    sumOfNum = sum(myList)
    print("The total is: " + str(sumOfNum))

sumList()
