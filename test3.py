#test3.py


'''The purpose of this test is to determine the following question:
In the multiple valued dictionary, is there ever a word where there are multiple
meters?

The answer to this question will determine whether there will be a change to the
library to attempt to make a function which will match the right word based on
meter to a poem when a poem is "updated".'''

import poetlibrary

for key in poetlibrary.poemclass.opendictionary.dictionary.keys():
    if len(poetlibrary.poemclass.opendictionary.dictionary[key]) > 1:
           print(key)

'''The results of the test is that each word only has one meter.'''


#I am going to try a much different method.  I am going to try to consolidate
#each dictionary value's list, and then afterwards, if any value list has more
#than one value, I will know there is a difference.  I am going to add a
#function to the mdict class

#def differences(a_list):
#    '''determine how many different elements are in the list'''
#    #each value is a different list
#    for n in x:
#        for o in range(0, len(x)):
#            if n == o:
#                continue
#            else:
#                return False
#    return True

#words_that_can_have_different_meter = 0



#for key in poetlibrary.poemclass.opendictionary.dictionary.keys():
#    x = []
#    for value in key:
#        x.append(value.getMeter())#

#    if (differences(x)):
#        continue
#    else:
#        words_that_can_have_different_meter += 1

#print(words_that_can_have_different_meter)
