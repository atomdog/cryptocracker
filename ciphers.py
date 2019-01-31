import hashlib
import base64
def enc_caesar(inpt, shift):
    newstr=""
    for x in range(0, len(inpt)):
        current = ((((ord(inpt[x])-97) + shift))%26)+97
        newstr+=(str(chr(current)))
    return(newstr)

def enc_md5(inpt):
    inpt = inpt.encode('utf-8')
    m = hashlib.md5()
    m.update(inpt)
    rv = m.hexdigest()
    #rv.decode("utf-8")
    return(rv)

def enc_base64(inpt):
    inpt = bytes(inpt, 'utf-8')
    rv = base64.encodestring(inpt)
    rv = rv.decode("utf-8")
    rv=rv[:-1]
    return(rv)
