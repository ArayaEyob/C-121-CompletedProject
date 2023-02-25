import random


def getWords(filename):
    file1 = open(filename)
    temp_list = list()

    for each_line in file1:
        each_line = each_line.strip()
        temp_list.append(each_line)

    words = tuple(temp_list)
    file1.close()

    return words


articles = getWords('articles.txt')
nouns = getWords('nouns.txt')
verbs = getWords('verbs.txt')
prepositions = getWords('prepositions.txt')


def sentence():
    return nounPhase() + "" + verbsPhase()


def nounPhase():
    return random.choice(articles) + " " + random.choice(nouns)


def verbsPhase():
    return random.choice(verbs) + " " + nounPhase() + " " + prepositionalPhase()


def prepositionalPhase():
    return random.choice(prepositions) + " " + nounPhase()


def main():
    number = int(input('enter number of a sentence:'))
    for count in range(number):
        print(sentence())


if __name__ == '__main__':
    main()

3
num = 0
with open('text.txt', 'r') as file:
    data = file.read()
    lines = data.split()
    num += len(lines)
print(num)


def countfreq(mylist):
    freq = {}
    for item in mylist:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    for key, value in freq.items():
        print("%d : % d" % (key, value))


if __name__ == '__main__':
    list1 = input("enter a file name")
    mylist = open(list1, "r")

