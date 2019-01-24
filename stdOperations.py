
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
