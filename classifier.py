import numpy as np
import fileCzar as fc


def sigmoid(x):
  y = 1/(1+np.exp(-x))
  return y

def dsigmoid(y):
  y = y*(1-y)
  return y

#increase by multiples of 2
#ileLib.validateExistence()
b = fc.fillTSet("testval.txt")

tr_arr_x = np.array(b[0])
tr_arr_y = np.array(b[1])
inputlayerthreadin = tr_arr_x
outputlayerthreadin = tr_arr_y

#inputlayerthreadin = np.array([[1,0,0,0,0,0],[0,0,1,0,0,0],[0,1,1,0,0,0],[0,0,0,0,0,1],[0,1,0,0,0,1],[1,1,1,1,1,1]])
#outputlayerthreadin = np.array([[0],[0],[0],[1],[1],[1]])

inputlayerpredict = np.array([0,0,0,1,0,0])
prediction = True
trainingtime = True
np.random.seed(1)



#weights
ih = 2*np.random.random((len(inputlayerthreadin[0]), len(inputlayerthreadin))) - 1
ho = 2*np.random.random((len(inputlayerthreadin), 1)) - 1
#ih, ho = fc.persistencein(ih, ho)
if(trainingtime == True):
    for enum in range(0,60000):

        ilayer = inputlayerthreadin
        hlayer = sigmoid(np.dot(ilayer, ih))
        olayer = sigmoid(np.dot(hlayer, ho))

        oerror = outputlayerthreadin - olayer
        odelta = oerror*dsigmoid(olayer)

        herror = odelta.dot(ho.T)
        hdelta = herror * dsigmoid(hlayer)

        ho += hlayer.T.dot(odelta)
        ih += ilayer.T.dot(hdelta)
    fc.persistenceout(ih, ho)






if(prediction == True):
  ilayer = inputlayerpredict
  hlayer = sigmoid(np.dot(ilayer, ih))
  olayer = sigmoid(np.dot(hlayer, ho))
  print(olayer)
