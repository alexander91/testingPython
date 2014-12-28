#import sl4a
from random import randrange
import os
import letterBase



class WordBuilder:
    def __init__(self):
        self.a = 'fignya'
    def getWord(self):
        result = ''
        length = 1 + randrange(5)
        for i in range(0,length):
            if (randrange(10) > 5):
                result = result + letterBase.getHardSyll()
            else:
                result = result + letterBase.getSoftSyll()
        return result







#droid = sl4a.Android()
print('Hello world!')
iterarr = [1, 2, 3, 4, 5]
astr = WordBuilder()
print(iterarr [2]);
user_input = ''
while (user_input != 'exit'):
    #astr.append('string at {0}'.format (I));
    #print (astr [I-1]);
    user_input = input('User: ')
    print ('Computer: ' + astr.getWord())
