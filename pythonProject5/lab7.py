# 1
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

# 2

hedges = ("please tell me more. ",
          "many of my patience tell me the same thing", "please coutinue")
qualifiers = ("why do you say that ", "you seem to think that,", "can you explain why ")

replacement = {"I": "you", "me": "you", "my": "your", "we": "you", "us": "you", "mine": "yours", "you": "I",
               "are": "am"}


def reply(sentence):
    probability = random.randit(1, 4)
    if probability == 1:
        return random.choice(hedges)
    return random.choice(qualifiers) + changePeron(sentence)


def changePerson(sentence1):
    words = sentence1.split()
    replyWords = []

    for i in range(len(words)):
        if words[i] == "you" and i < len(words) - 1 and words[i + 1] == "are":
            replyWords.append(replacement.get)
            replyWords.append(replacement.get("are", "are"))
        elif word[i] == "are" and i > 0 and words[i - 1] != "you":
            replyWords.append("are")
        elif words[i] == "are" and i > 0 and words[i - 1] == "you":
            continue

        else:
            replyWords.append(replacement.get(words[i], words[i]))

    return " ".join(replyWords)


def main():
    print("good morning, i hope you are well today.")
    print("what can i do for you?")

    while True:

        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("have a nice day")
            break
        print(reply(sentence))


if __name__ == '__main__':
    main()

# 3
import string
from string import punctuation

with open('test.txt', 'r') as file:
    text = file.read()
    text = text.lower()
    # remove punctuation in string
    cleaned_text = ""
    for i in text:
        if i in string.punctuation:
            text = text.replace(i, "")
    text = text.split()
    print(text)

    freq = {}
    for i in text:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    print(freq)
    print(freq.items())
    print(sorted(freq.items()))
