#https://www.codewars.com/kata/where-my-anagrams-at/train/python

def anagrams(word, words):
    anagrams = []
    for w in words:
        if ''.join(sorted(w)) == ''.join(sorted(word)):
            anagrams.append(w)
    return anagrams
