from scipy.sparse import *
import numpy as np
import time


def p2_has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not
    '''
      HINT: You can `print(sets)` to show what the matrix looks like
        If we have a directed graph with 2->3 4->1 3->5 5->2 0->1
               0  1  2  3  4  5
            0  0  1  0  0  0  0
            1  0  0  0  0  0  0
            2  0  0  0  1  0  0
            3  0  0  0  0  0  1
            4  0  1  0  0  0  0
            5  0  0  1  0  0  0
        The size of the matrix is (6,6)
    '''
    #starttime = time.time()
    sets = csr_matrix(sets)
    #print(sets.shape)
    setsize = sets.shape[0]
    i = 0
    temp = sets
    while i < setsize:
	temp = temp.dot(sets)
	check = (temp.diagonal() == 1)
        if check.any():
            #endtime = time.time()
            #print (endtime - starttime)
            return True              
        i += 1
    #endtime = time.time()
    #print (endtime - starttime)    
    return False
