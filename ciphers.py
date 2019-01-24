import hashlib
def caesar(inpt, shift):
    newstr=""
    for x in range(0, len(inpt)):
        current = ((((ord(inpt[x])-97) + shift))%26)+97
        newstr+=(str(chr(current)))
    return(newstr)
def md5hash(inpt):
    inpt = inpt.encode('utf-8')
    m = hashlib.md5()
    m.update(inpt)
    rv = m.hexdigest()
    #rv.decode("utf-8")
    return(rv)
