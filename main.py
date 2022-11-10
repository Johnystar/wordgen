LVL1 =        'arst' + 'neio'
LVL2 = LVL1 + 'gm'
LVL3 = LVL2 + 'pbjl'
LVL4 = LVL3 + 'cdvk'
LVL5 = LVL4 + 'wf' + 'uy'
LVL6 = LVL5 + 'q' + 'zx' + 'h'

allowed_symbols = LVL3

n_of_words = 50







from random import randrange

words = []

with open('words.txt', 'r') as f:
    for word in f:
        word = word.lower()
        word = word.replace('\n', '')

        if len(word) <= 1: continue
        if word in words: continue
        if not all(char in allowed_symbols
                   for char in word): continue

        words.append(word)

assert len(words) >= n_of_words


output = []

while len(output) < n_of_words:
    output.append(words.pop(randrange(len(words))))

print(' '.join(output))
print(len(output))
