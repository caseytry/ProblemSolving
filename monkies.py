import random

def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(26)]
        
    return res


#print(generateOne(28))

def score(goal, teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame = numSame + 1
    return numSame / len(goal)

#print(score("methinks it is like a weasle", generateOne(28)))


def main():


    goalstring = 'methinks'
    newstring = generateOne(8)
    best = 0
    newscore = score(goalstring, newstring)
    loops = 0

    while newscore < 1:
        newstring = generateOne(8)
        if newscore >= best:
            print(newscore, newstring)
            best = newscore
        newstring=generateOne(8)
        newscore= score(goalstring, newstring)
        loops += 1
        if (loops % 100000) == 0:
                print(loops)

main()
