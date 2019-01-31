
import stdOperations
import ciphers
ciphertext =[]
strtest= "sample english text"
for x in range(0, 25):
    ciphertext.append(ciphers.enc_caesar(strtest,x))
ciphertext.append(ciphers.enc_base64(strtest))
ciphertext.append(ciphers.enc_md5(strtest))
print(ciphertext)
inputw=[]
for x in range(4,5):
    inputw.append(stdOperations.measureAgainstEnglish(ciphertext[x]))
    inputw.append(stdOperations.normalizeUniqCount(stdOperations.characterCountNumerical(ciphertext[x])))
    inputw.append(stdOperations.ioc(ciphertext[x]))
print(inputw)
