#opendictionary.py

#opendictionary module opens the dictionary for use in the poemclass module.
# if it cannot open the dictionary, it will summon the parseDictionary module
# to parse a new dictionary.

#Since the dictionary will be open in this module, any functions which directly
#affect the dictionary, which is presently just the getWordFromDictionary
#function, will be in this module.

#I am not sure at the moment why the parseString function is in this module.
#I might make a new parse module and place the function to
#parse the dictionary lines and parseString into it.

import pickle
import re
import wordclass
import sys

#see if the dictionary exists as a pickled file.
#if dictionary exists:
#do stuff
#else
#if cmudict.txt exists:
#parse it
#do this all from the parseDictionary module

try:
    #dictionary is going to have all of the wordclass objects in it.
    pickled_dictionary = open("dictionary.pkl", 'rb')
    dictionary = pickle.load(pickled_dictionary)
    pickled_dictionary.close()
    
except IOError:
    print("cannot open dictionary!!! creating the dictionary from file")
    #If the pickled dictionary doesn't exist, then create one!
    try:
        import parseDictionary
    except IOError: #re-raised in parseDictionary
        sys.exit("Cannot find the dictionary -- cannot parse")

    #Now that the dictionary has theoretically been parsed, try to open it
    #-- I am sure that the error checking here can be made much "safer"

    try:
        pickled_dictionary = open("dictionary.pkl", 'rb')
        dictionary = pickle.load(pickled_dictionary)
        pickled_dictionary.close()

    #If it cannot be found, then there is a problem, most likely, with the
    #parse dictionary module so look there.
    except IOError:
        print("cannot open dictionary!!!")
        sys.exit("Cannot find the pickled file -- canot parse")



def getWordFromDictionary(input_word):
    '''Return the first instance of the word'''
    '''This will be changed later to search through the whole array of possible
        values, looking for a word depending on rhyme and/or meter'''
    input_word = input_word.lower()

    try:
        return dictionary[input_word][0][0]
    #if it is not in the dictionary.
    except KeyError:
        #This is going to create a wordclass object which has the word
        # as its text but has meter of -1, 1 syllable, and no rhyme
        #(Should it have -1 syllable to keep up with "convention"?)
        # The false parameter means it was not found in the dictionary.
        
        return wordclass.WordClass(input_word, False)

def parseString(string):
    '''Use python's re to return all "potential words" in a string'''
    return re.findall(r"[\w']+", string)
    #print(string)
    #return re.findall(r"(?=.*\w)^(\w|')+$", string)
