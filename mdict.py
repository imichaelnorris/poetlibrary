#mdict.py
#The purpose of this class is to have a dictionary of wordclass objects
#with multiple wordclass objects for certain words stored into a list.
#This way, certain functions can look through every instance of a word by
#using a word as the key to access the list.

#Right now there seems to be a strange amount of list layers (not sure if this
#is correct because I haven't done any investigating into it).
#There is usually one more than it seems like there should be.
#This occurs between pickling the dictionary and unpickling it.



class mdict(dict):
    '''This dictionary will have multiple values for a specific key.
           The keys will be words, and the values wordclass objects.'''
    def __setitem__(self, key, value):
        self.setdefault(key, []).append(value)
