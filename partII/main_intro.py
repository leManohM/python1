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
    # pour decrypter on utilise -shift qui revient a la translation inverse

#Build an RPG character
#freeciodecamp.org exercise solultion i made 

full_dot = '●'
empty_dot = '○'
def check_name(name):
    """ Check the validity of a character name.
    The name should be a string without spaces, not empty, and no longer than 10 characters."""
    if not isinstance(name, str):
        return "The character name should be a string"
    if " " in name : 
        return "The character name should not contain spaces"
    if not name :
        return "The character should have a name"
    if len (name)> 10:
        return "The character name is too long"
    
    
        

def create_character(name,strength,intelligence,charisma):
    if check_name(name) != None:  #if the name is not valid i return the error
        return check_name(name)
    #else i check the stats
    stat =  [strength,intelligence,charisma]
    for para in stat:#check each stat validity individually
        if not isinstance(para , int):
            return "All stats should be integers"
        if para < 1 :
            return "All stats should be no less than 1"
        if para > 4 :
            return "All stats should be no more than 4"
    if sum(stat) != 7 :
        return "The character should start with 7 points"
    return name+"\n"+"STR "+"●"*strength+"○"*(10- strength)+"\n"+"INT "+"●"*intelligence+"○"*(10- intelligence)+"\n"+"CHA " +"●"*charisma +"○"*(10- charisma)


