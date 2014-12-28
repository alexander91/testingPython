from random import randrange

hardLetters = ['s', 'g', 'p', 'th', 'ch', 'q', 'b', 'n','t','k']

softLetters = ['a', 'e', 'u', 'o', 'i']

    
def getSoftSyll():
    i = randrange( len(hardLetters) )
    j = randrange( len(softLetters) )
    
    return hardLetters[i] + softLetters[j]

def getHardSyll():
    i = randrange( len(hardLetters) )
    j = randrange( len(softLetters) )
    
    return softLetters[j] + hardLetters[i]
    
    
    
    
def AddSoftLetter(newSoft):
    global softLetters
    softLetters.append(newSoft)
    
    
    
def AddHardLetter(newHard):
    global hardLetters
    hardLetters.append(newHard)
    
    
    
def AddFromSyllableWithArray(syllable, array, otherArray):
    for letter in array:
        if syllable.find(letter) == 0:
            otherArray.append(syllable[len(letter):])
            return True
    return False
    
def AddFromSyllable(syllable):
    global softLetters
    global hardLetters
    
    if AddFromSyllableWithArray(syllable, softLetters, hardLetters):
        return
    
    AddFromSyllableWithArray(syllable, hardLetters, softLetters)

            
        
            