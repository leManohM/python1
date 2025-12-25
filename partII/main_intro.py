#here to build the main intro for part II
#and  doing the ceasaer cipher

#it counts the letters in a word
def counter_iteration_letter(word):
    res=dict()
    for letter in word:
        res[letter]=res.get(letter,0)+1
    return res