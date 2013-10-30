import poetlibrary

#This test is going to throw all of the text into the poem form object at once
# -You can also put each word in individually as well.

iambicPentameter = poetlibrary.forms.PoemStyle("iambic pentameter",
                                               [0, 1], 5, 14)

newPoem = poetlibrary.Poem(iambicPentameter, "Sonnet XIII",
                           "William Shakespeare")

#I am going to use the setText function which takes in a two-dimensional list
#with the first dimension holding lists which are the successive lines of a
#poem
poemText = []
for n in range(0, iambicPentameter.getLines()):
    poemText.append([])

#Neither O or Oh are in the dictionary (I haven't actually searched but I
#think that I remember that they are not)? Rectify this madness.
poemText[0] = ["O that you were yourself but love you are"]
#poemText[0] = ["Oh that you were yourself but love you are"]
poemText[1] = ["No longer yours than you yourself here live"]
poemText[2] = ["Against this coming end you should prepare"]
poemText[3] = ["And your sweet semblance to some other give"]
poemText[4] = ["So should that beauty which you hold in lease"]
poemText[5] = ["Find no determination then you were"]
poemText[6] = ["Yourself again after yourself's decease"]
poemText[7] = ["When your sweet issue your sweet form should bear"]
poemText[8] = ["Who lets so fair a house fall to decay"]
poemText[9] = ["Which husbandry in honour might uphold"]
poemText[10] = ["Against the stormy gusts of winter's day"]
poemText[11] = ["And barren rage of death's eternal cold"]
poemText[12] = ["O none but unthrifts Dear my love you know"]
#poemText[12] = ["Oh none but unthrifts Dear my love you know"]
poemText[13] = ["You had a father let your son say so"]

#newPoem.addText(poemText)
newPoem.setText(poemText)


#Which words were not in the dictionary?
#for line in newPoem.text:
#    for word in line:
#        if not word.getIsInDictionary():
#            print(word.getWord())



#This function returns a list - [percentage of words matching meter, words
#                                that are not in the dictionary]
adherance = newPoem.getMeterAdherancePercentage()
adherance_percentage = str(adherance[0] * 100)
words_without_meter = str(adherance[1])

#newPoem.printText()

#Metrical adherance
print("The poem " + newPoem.getTitle() + " by " + newPoem.getAuthor())
print("was scanned and its metrical adherance to " +
      newPoem.poemFormObject.getMeterName())
print("is " + adherance_percentage + " percent.")
print("This does not include the " + words_without_meter + " words that")
print("were not in the CMU dictionary")
