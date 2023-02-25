# take the input
filename = input("enter the file name: ")
inputfilename = open(filename, 'r')

text = inputfilename.read()

# count the sentences

sentences = text.count('.') + text.count('?') + \
    text.count('!') + text.count('i') + \
    text.count('!')

# count the words

words = len(text.split())
# count the syllables
syllables = 0
vowels = "AaEeIiOoUu"
for word in text.split():
    for vowels in vowels:
        syllables += word.count(vowels)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
        if word.endswith('le'):
            syllables += 1

# compute the flesch index and grade level

index = 206.835 - 1.015 * (words/sentences) - 84.60 * (syllables / words)

level = round(0.39 * (words / sentences ) + 11.8 * (syllables / words) - 15.59)
print("the flesch index is", index)
print("the Grade level equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")