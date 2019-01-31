import numpy as np
from scipy import spatial
def characterCount(inpt):
    uniqueCharacterList = []
    for x in range(0, len(inpt)):
        doesExist = False
        for x2 in range(0, len(uniqueCharacterList)):
            if(inpt[x]==uniqueCharacterList[x2]):
                doesExist = True
        if(doesExist == False):
            uniqueCharacterList.append(inpt[x])
    return(uniqueCharacterList)

def characterCountNumerical(inpt):
    uniqueCharacterList = []
    for x in range(0, len(inpt)):
        doesExist = False
        for x2 in range(0, len(uniqueCharacterList)):
            if(inpt[x]==uniqueCharacterList[x2]):
                doesExist = True
        if(doesExist == False):
            uniqueCharacterList.append(inpt[x])
    return(len(uniqueCharacterList))


def uniqCharacterCount(inpt, schar):
    counter = 0

    for x2 in range(0, len(inpt)):
        if(schar==inpt[x2]):
            counter+=1
    return(counter)

def cleanInputAlphabetical(inpt):
    inpt = inpt.lower()
    rv = []
    for x in range(0, len(inpt)):
        if((97<=ord(inpt[x])<=123)):
            rv.append(inpt[x])
    return(rv)

def ioc(inpt):
    inpt = cleanInputAlphabetical(inpt)
    summation = 0
    for x in range(97, 123):
        strevaluation = str(chr(x))
        fi = uniqCharacterCount(inpt, strevaluation)
        summation = summation + (fi*(fi-1))
    finalresult = summation/ (len(inpt)*(len(inpt)-1))
    return(finalresult)

def onegram(inpt):
    #alphabeticfreq = [8.167, 1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    storedcount = [0] * len(letters)
    for x in range(0, len(letters)):
        counter=0
        for y in range(0, len(inpt)):
            if(inpt[y]==letters[x]):
                counter+=1
        storedcount[x] = counter/len(inpt)
    #print(letters[np.argmax(storedcount)])
    return(storedcount)

def measureAgainstEnglish(inpt):
    alphabeticfreq = [8.167, 1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
    comparison = onegram(inpt)
    cosinesimilarity = 1 - spatial.distance.cosine(alphabeticfreq, comparison)
    return(cosinesimilarity)

def normalizeUniqCount(inpt):
    normalizedvalue = (inpt - 2)/(30-2)
    return(normalizedvalue)
