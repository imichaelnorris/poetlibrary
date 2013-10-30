import poetlibrary

#This test is going to demonstrate inserting words individually
#into the poem object.
#I am going to place the text of the poem into a two dimensional list
#and then iterate over the list and remove each word individually

iambicPentameter = poetlibrary.forms.PoemStyle("iambic pentameter",
                                               [0, 1], 5, 14)

newPoem = poetlibrary.Poem(iambicPentameter, "Sonnet XCIV",
                           "William Shakespeare")

#text seperating each row into its own string
text = ["They that have power to hurt and will do none,",
        "That do not do the thing they most do show,",
        "Who, moving others, are themselves as stone,",
        "Unmoved, cold, and to temptation slow;",
        "They rightly do inherit Heaven's graces,",
        "And husband nature's riches from expensive;",
        "They are the lords and owners of their faces,",
        "Others but stewards of their excellence.",
        "The summer's flower is to the summer sweet",
        "Though to itself it only live and die;",
        "But if that flower with base infection meet,",
        "The basest weed outbraves his dignity:",
        "For sweetest things turn sourest by their deeds:",
        "Lilies that fester smell far worse than weeds."]

poemText = []
for n in text:
    poemText.append(poetlibrary.poemclass.opendictionary.parseString(n))


#print(poemText)

#add the words
for i in range(0, len(poemText)):
    for j in range(0, len(poemText[i])):
        newPoem.addText(poemText[i][j], i, j)


#print("Which words were not in the dictionary?")
#for line in newPoem.text:
#    for word in line:
#        if not word.getIsInDictionary():
#            print(word.getWord())


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
