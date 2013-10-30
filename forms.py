#forms.py

#The forms module holds the PoemStyle class.  This class's intended use is the
# to hold a meter for a specific poem and hold a rhyme scheme.  This class will
# be used by the poem class to compare its meter to a certain PoemStyle's
# meter (checking adherance to the defined meter).

# Parts of the poem class that have not been implemented are the following:
# supporting rhyming (putting a phoneme on certain syllables)
#  -- Note about rhyming.  I imagine that the way a rhyme scheme will be held
#     in this class is that, if, for instance, the rhyming scheme is ABBA,
#     this class will keep track of which words in which lines are supposed
#     to rhyme together (don't assume only the end word on a line will rhyme)
#     Somewhere else (the poemclass module, maybe) will hold a function which
#     compares two words to see if they rhyme.
#     When checking rhyme, first the PoemStyle member function will be called
#     to see which words need to be checked (based on their meter, I think -
#     although maybe it will be based on which number word they are).
#     --it would assume only one rhymed word per line, so you call the function
#       with a line number and it returns which syllable that line needs to
#       match with on which other line.

class PoemStyle:
    '''A PoemStyle holds the meter of the certain syllables in a poem and
        will, in the future, keep track of rhyme adherance.'''
    def __init__(self, name, foot, feetPerLine, lines):
        '''Meter is a list of one "foot".  Length is
            the total amount of FEET per line.'''
        #There should be two names, one for the meter, one for the rhyme?
        #(Rhyme when I implement it)
        #--- think about having algorithmically created feet
        if type(name) != str:
            raise ValueError
        if type(foot) != list:
            raise ValueError
        if type(feetPerLine) != int:
            raise ValueError
        if type(lines) != int:
            raise ValueError

        self.meterName = name
        
        self.foot = foot
        self.footSyllables = len(foot)
        self.feetPerLine = feetPerLine
        self.syllablesPerLine = self.footSyllables * feetPerLine
        self.lines = lines

        #meterList has an element of the list for each syllable
        self.meterList = [foot * feetPerLine]*lines

    def getMeterName(self):
        '''return the name of the meter'''
        return self.meterName
    def getFoot(self):
        '''return the meter, or one foot'''
        return self.foot
    def getFeetPerLine(self):
        '''return the amount of feet per line'''
        return self.feetPerLine
    def getSyllablesPerLine(self):
        '''return the amount of syllables per line'''
        return self.syllablesPerLine
    def getLines(self):
        '''return the amount of lines'''
        return self.lines
    def getMeterList(self):
        '''return the meter list'''
        return self.meterList
    def getMeterListByIndex(self, line, syllable):
        '''returns the meter in the fullMeter list at the element
            self.meterList[line][syllable] --- '''
        try:
            return self.meterList[line][syllable]
        except IndexError:
            print("No meter for this syllable", line, syllable)
            return -2
        
#iambic_pentameter = PoemStyle("Iambic Pentameter", [0, 1], 5, 14)
iamb = [0, 1]
trochee = [1, 0]
dactyl = [1, 0, 0]
anapest = [0, 0, 1]
amphibrach = [0, 1, 0]

monometer = 1
dimeter = 2
trimeter = 3
tetrameter = 4
pentameter = 5
hexameter = 6
heptameter = 7
octameter = 8

#tests
#a = PoemStyle("Iambic Pentameter", [0, 1], 5, 14)
#a = PoemStyle("Iambic Pentameter", iamb, pentameter, 14)

