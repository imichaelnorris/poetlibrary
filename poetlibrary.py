#poetlibrary.py

#This is going to be the only file that you will want to import.
#There is more information about the other classes in their modules
#and in the readme.

#This library enables you to write and/or analyze a poem and test its adherance
#to a poetic meter.  The next tidbit of functionality that will be added is
#going to be rhyme, which some is a fundamental aspect for a versatile
#library for poems.  But for now, you can mess around with meter.  Enter in
#some Shakespeare, and lambast his flaws.  For help understanding how to
#implement the library, look at any of the files whose names begin with "test"

import forms
import mdict
import poemclass
from poemclass import Poem


#Do not import the wordclass module because it is an "under the hood" module
#import wordclass

#if there is any other code that I need to do to initialize the modules,
#do it here.




#iambicPentameter = forms.PoemStyle("iambic pentameter", [0, 1], 5, 14)

#newPoem = Poem(iambicPentameter)

#newPoem.addText("hello", 0, 0)
