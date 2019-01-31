import numpy as np
def fillTSet(filename):
    tr_arr_x = []
    tr_arr_y = []
    x = True

    with open(filename, 'rU') as readinfile:
        for line in readinfile:
            #load line in as string to be parsed
            linestred = line
            if(x == True):
                 tr_arr_x.append([])
                 tr_arr_x[len(tr_arr_x)-1] = linestred.split(",")
                 for enum in range(0, len(tr_arr_x[len(tr_arr_x)-1])):
                     tr_arr_x[len(tr_arr_x)-1][enum] = int(tr_arr_x[len(tr_arr_x)-1][enum])
            if(x == False):
                tr_arr_y.append([int(linestred)])
            x = not x
    return([tr_arr_x, tr_arr_y])

def persistenceout(wih, who):
    np.save('wih_cache', wih)
    np.save('who_cache', who)
def persistencein(wih, who):
    wih = np.load('wih_cache.npy')
    who = np.load('who_cache.npy')
    return(wih, who)
