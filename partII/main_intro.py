#here to build the main intro for part II
#and  doing the ceasaer cipher

#it counts the letters in a word
def counter_iteration_letter(word):
    res=dict()
    for letter in word:
        res[letter]=res.get(letter,0)+1
    return res
print(counter_iteration_letter("hello world"))

#it s now the caesar cipher
def caesar_cipher(text, shift):
    #verify that shift is an integer
    if not isinstance(shift, int):
        raise ValueError("Shift must be an integer")

    #shift is the number of positions to shift
    alphabet = 'abcdefghijklmnopqrstuvwxyz' #the alphabet
    shifted_alphabet = alphabet[shift:] + alphabet[:shift] #the shifted alphabet
    translation_table = str.maketrans(alphabet, shifted_alphabet)#the translation table of the alphabet to the shifted alphabet
    return text.translate(translation_table) #return the translated text