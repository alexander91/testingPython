from random import randrange

knownSyllables = ['pa']
syllablesUsage = [0]
totalUsageOfDatabase = 0

def AddSyllable(newSyllable):
    global knownSyllables
    knownSyllables.append(newSyllable)
    syllablesUsage.append(0)
    
def SyllsAvailibale():
    if (totalUsageOfDatabase/len(knownSyllables) < 2):
        return True
    return False

def GetKnownRandomSyll():
    return knownSyllables[randrange(len(knownSyllables) - 1)] 

def GetSyll():
    if (SyllsAvailibale()):
        return GetKnownRandomSyll()
        
    
def GetWord(numOfSyll):
    
    for i in range(numOfSyll):
        result = result + letterBase.getHardSyll()