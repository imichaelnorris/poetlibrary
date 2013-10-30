#parseDictionary.py
#NOTE: The object dictionary is a python object dict of a "real dictionary"

import wordclass
import pickle
import mdict

#see if the dictionary exists as a pickled file.
#if dictionary exists:
#pass
#else
#if cmudict.txt exists:
#parse it
#do this all from the parseDictionary module


try:
    dictionaryFile = open("cmudict.0.7a.txt", "r")
except IOError:
    print("Cannot open cmudict.0.7a.txt. Terminating...")
    raise #IOError

a = dictionaryFile.readline()

#Get to the point where the dictionary begins
#--I included the proceeding text to denote that location
while (a != "//BREAK-BEGIN-LIST//\n"):
    a = dictionaryFile.readline()

dictionary = mdict.mdict() #allows multiple values per key

while (a != ''):
    a = dictionaryFile.readline()

    #create an instance of a WordClass object
    newObject = wordclass.WordClass(a)

    #This should throw the newObject into the dictionary.
    try:
        temp = dictionary[newObject.getWord()]
        for i in temp:
            #If they are the same, then I do not want to put the word in there
            if newObject == i:
                break
            else:
                continue    
        dictionary[newObject.getWord()] = newObject
    except KeyError:
        dictionary[newObject.getWord()] = newObject
    
#pickling the dictionary.
output = open("dictionary.pkl", 'wb')
pickle.dump(dictionary, output)
output.close()
