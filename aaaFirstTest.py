import sl4a
from random import randrange
import os

class Syllable:
    def __init__(self):
        self.soft = ['a', 'e', 'u', 'o', 'i']
        self.hard = ['s', 'g', 'p', 'th', 'ch']
        self.ready = []
        
    def getSyll(self):
        i = randrange(len(self.soft))
        j = randrange( len(self.hard) )
        return self.hard[j] + self.soft[i]

        
    

class WordBuilder:
    def __init__(self):
        self.mySyll = Syllable()
    def getWord(self):
       result = ''
       length = 1 + randrange(5)
       for i in range(0,length):
           result = result + self.mySyll.getSyll()
       return result







droid = sl4a.Android()
print('Hello world!')
iterarr = [1, 2, 3, 4, 5]
astr = WordBuilder()
print(iterarr [2]);
for I in range(1, 15):
    #astr.append('string at {0}'.format (I));
    #print (astr [I-1]);
    print (astr.getWord())
