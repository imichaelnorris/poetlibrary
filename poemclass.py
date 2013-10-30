#poemclass.py
#A Poem object consists of the text of a poem. When text is placed in the Poem
# object you can presently check to see the meter of the poem.

import forms
import wordclass

#This import puts the dictionary in the namespace of opendictionary. 
import opendictionary
#opendictionary.dictionary['word'][0][0].getMeter()


#This function calls the getWordFromDictionary function in the opendictionary
# module
def getWordFromDictionary(input_word):
    '''returns the first wordclass object from dictionary that has the
        key, "word"'''
    '''This calls the function of the same name from the
        opendictionary module'''
    return opendictionary.getWordFromDictionary(input_word)
def parseString(string):
    '''Parse the string to include only lower case letters'''
    return opendictionary.parseString(string)
    
#I noticed a discrepancy: The Poem classes meter is called meter and the form
# class's meter is called meterList.  Reconcile this.
class Poem:
    '''A Poem Object contains one poem and its adherence to a Poem Form'''
    '''It should be noted that any program that is going to be creating a
        Poem should keep track of the length of each line and where the cursor
        currently is so words can be appended, inserted, and deleted.
        Any time a word is changed, you may want to update the text.'''
    def __init__(self, poemFormObject, title = "", author = ""):
        '''create a blank poemClass'''
        self.poemFormObject = poemFormObject

        #This will be two dimensional.  First dimension is line, second
        #dimension is WordClass object
        self.meter = [[]]
        #self.text = [[]] * poemFormObject.getLines()
        self.text = [[] for n in range(0, poemFormObject.getLines())]
        self.textLength = len(self.text)

        self.title = title
        self.author = author
    def setText(self, t):
        '''Overwrites the text with the 2-d List "t" that is passed in.
            This function assumes the text, t, that is passed into it is
            formatted in accordance with the desired poem form.'''
        '''This
            means that t is a two-dimensional list, with each inner-
            list being a "line" of text - a line according
            to the poem form.'''
        #This loop should take each word string from "t" and place its
        # wordclass object into self.text, overwriting any words.
        #for n in range(0, len(t)):
        #    for o in range(0, len(t[n])):
        #        self.text[n].insert(o, getWordFromDictionary(t[n][o]))

        #t must be a two-dimensional list
        for n in range(0, len(t)):
            if len(t) > self.poemFormObject.getLines():
                break
            word_list = parseString(t[n][0])
            for a_word in word_list:
                self.addText(a_word, n, len(self.text[n]))
    def addText(self, input_word, line, word_pos):
        '''Pass in a word string (not a wordclass object), the line number,
           and the position of the word and this function will place it in
           self.text in the respective area.'''
        '''The following array of words (remember that text is full of
            wordclass objects, not words) will have word_pos of 1, 2, and 3.
            ['hello', 'my', 'world']
            Now, if you want to insert a word to the beginning, the index will
            be 0.  To the end, the index will be 4.'''
        self.text[line].insert(word_pos, getWordFromDictionary(input_word))
    def printText(self):
        '''prints all of the text'''
        for n in self.text:
            for o in n:
                print(o.getWord())
    def deleteWord(self, line, word_pos):
        '''Delete a word given a line number and a word_pos number'''
        #If there are less lines of text in the object than the argument
        # "line", then I do not want to attempt to delete the word because
        # it is not in the poem.
        if len(self.text) < line:
            return
        if len(self.text[line]) < word_pos:
            return
        del(self.text[line][word_pos])
    def updateMeter(self):
        '''This function updates the meter list of the poem'''
        self.meter = []
        for n in range(0, len(self.text)):
            self.meter.append([])
            for o in range(0, len(self.text[n])):
                self.meter[n] += self.text[n][o].getSyllableArray()
    def getMeter(self):
        '''return the meter of all of the words in the poem compared to the
            poemFormObject.'''
        return self.meter
    def checkMeter(self):
        '''Compare self.meter with poemFormObject.getMeterList()'''
        #This needs to be made to check regardless of line amount or length,
        #which shouldn't take too long.
        if (self.getMeter() == self.poemFormObject.getMeterList()):
            return True
        return False
    def getMeterAdherancePercentage(self):
        '''Return a list holding the amount of metrical syllables from the
            poem that match the poemFormObject's meter and the amount of words
            in the poem that are not a part of the CMU dictionary.'''
        #Note that this function automatically updates the poem's meter
        self.updateMeter()
        meter = self.getMeter()
        accurate = 0
        total = 0
        words_without_known_meter = 0
        for i in range(0, len(meter)):
            for j in range(0, len(meter[i])):
                if meter[i][j] == self.poemFormObject.getMeterListByIndex(i,j):
                    accurate += 1
                    total += 1
                elif meter[i][j] == -1:
                    #Don't increase the total, because you can't compare
                    #a word whose meter you do not know.
                    words_without_known_meter += 1
                else:
                    total += 1
        #return (accurate / total)
        return [(accurate / total), words_without_known_meter]

    def getAuthor(self):
        '''return the author'''
        return self.author
    def getTitle(self):
        '''return the title'''
        return self.title
    def setAuthor(self, val):
        '''set the author'''
        self.author = val
    def setTitle(self, val):
        '''set the title'''
        self.title = val
    

#newForm = forms.PoemStyle("iambic pentameter", [0, 1], 5, 14)
#newPoem = Poem(newForm, "something", "me")
#newPoem.setText([["this could be an everlasting love for me"], ['something']])
