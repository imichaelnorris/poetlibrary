#wordclass.py

#A WordClass object contains a word and its poetic meter.  In the future it
#will carry the rhyme of a word, which will most likely be the last or one
# of the last sounds that it makes according to the phonemes which are in the
# CMU dictionary.

#The WordClass object is the fundamental piece of the poetlibrary.
#I am thinking of changing the class name to "Word", assuming there is
#nothing else that is generally usually a "word" in python.

def consolidateSecondaryStress(x):
    '''pass in the list x, with syllable stresses as its values and it
        will convert all of the secondary stresses, the 2's, into 0's'''
    ''' Note that making the secondary stresses not count as stress is
        completely arbitrary.  They could also be counted as stresses.
        This maneuver is to simplify things in the early stages of
        development.'''
    for n in range(0, len(x)):
        if x[n] == 2:
            x[n] = 0

def parseStringToWord(string):
    '''Take in a string from the CMU dictionary and return a list that
        contains all of the values necessary to initialize a WordClass
        object.'''
    text = string

    #I believe that I can remove the preceeding line because I also had
    # to put it in the opendictionary module
    text = text.lower()

    #Now I am using word as the key, and key is a unique identifier.
    #word corresponds to a spelling and key corresponds to the word
    # and properties (meter).
    for n in range(0, len(text)):
        if text[n] == " ":
            word = text[0:n]
            syl = text[n:]
            break

    syllables = 0
    syllableArray = []

    #If there are multiple words in the dictionary with the same spelling,
    #they will have parentheses and a number (#) to distinguish different
    #instances of the word
    for n in range(0, len(word)):
        if word[n] == "(":
            word = word[0:n]
            break
        
    #The identifier is going to be the word plus its syllables (as 0, 1, 2)
    #In the future, when I implement rhyme, I am going to have to change
    #this to have words' keys being the word plus phoenemes plus
    #syllables. (although I might be able to disregard syllables because
    #at that point, all words might be unique with just word+phonemes
        
    identifier = word

    #This is getting the amount of syllables by counting how many numbers
    #are in the string: 0 indicates unstressed, 1 indicates primary stress,
    #2 indicates secondary stress.
    for n in syl:
        if n == "0" or n == "1" or n == "2":
            syllables += 1
            syllableArray.append(int(n))
            identifier += n
    #for now, I am going to ignore the secondary stress as it relates to
    #a poem, so I am going to call this function to disregard it.
    #all 2's are turned to zero
    consolidateSecondaryStress(syllableArray)

    return [word, syllables, syllableArray, identifier, True]    

class WordClass:
    '''A WordClass object holds a word and its poetic meter'''
    def __init__(self, text='', isInDictionary=True):
        '''Initialize a WordClass object by taking the passed in text
            and extracting the necessary information from it.'''
        if text == '':
            # I am not sure if this "empty word" is needed, but I am going
            # to include it anyway, for now.
            self.word = text
            self.syllables = 0
            self.syllableArray = []
            self.identifier = ''
            self.isInDictionary = False
            return
        if not isInDictionary:
            self.word = text
            self.syllables = 1#If you do not know the syllables, make it ONE
            self.syllableArray = [-1] #a meter of -1 is UNKNOWN
            self.identifier = text
            self.isInDictionary = isInDictionary
            return
        
        #if one of the first if blocks do not trip it, then it is presumed
        #to be a line from the CMU dictionary.
        temp_list = parseStringToWord(text)
        
        self.word = temp_list[0]
        self.syllables = temp_list[1]
        self.syllableArray = temp_list[2]
        self.identifier = temp_list[3]
        self.isInDictionary = temp_list[4]
    def __eq__(self, right):
        '''Determine if the a word and its meter is identical to another word
            and its meter'''
        if self.getIdentifier() == right.getIdentifier():
            return True
        return False
    def getWord(self):
        '''return self.word'''
        return self.word
    def getSyllables(self):
        '''return the amount of syllables in the word'''
        return self.syllables
    def getSyllableArray(self):
        '''return the syllables of the word'''
        return self.syllableArray
    def getIdentifier(self):
        '''return the unique identifier for the word'''
        return self.identifier
    def getIsInDictionary(self):
        return self.isInDictionary

#bob = WordClass("salamander(1) s1 0 0 0")
#print(bob.getWord())
#print(bob.getSyllables())
#print(bob.getSyllableArray())
#print(bob.getKey())
