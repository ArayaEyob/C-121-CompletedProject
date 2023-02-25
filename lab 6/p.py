import random


def words(filename):
    with open(filename) as f:
        Word1 = f.read().strip().split()
    return tuple(Word1)


articles = words('articles.txt')
nouns = words('nouns.txt')
verbs = words('verbs.txt')
prepositions = words('prepositions.txt')

print(articles)
