from scipy.sparse import *
import numpy as np
import time

def p1_has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not
    '''
      HINT: You can print(sets) to show what the matrix looks like
        If we have a directed graph with 2->3 4->1 3->5 5->2 0->1
               0  1  2  3  4  5
            0  0  0 -1  1  0  0
            1  0  1  0  0 -1  0
            2  0  0  0 -1  0  1
            3  0  0  1  0  0 -1
            4 -1  1  0  0  0  0
        The size of the matrix is (5,6)
    '''
    #starttime = time.time()
    idx = 0
    data = csr_matrix(sets)
    datasize = data.shape[0]
    #print(data.shape)
    while datasize >= 1: 
      if data[idx][0].data[0] == -1:
	rewrite = (data.T[data[idx][0].indices[1]].A == -1)[0]     
      else:
	rewrite = (data.T[data[idx][0].indices[0]].A == -1)[0]     
      rewrite_arr = data[rewrite] 
      if rewrite_arr.shape[0] != 0: 
        rewrite_arr = vstack(((data[idx], rewrite_arr)))
        idty = identity(rewrite_arr.shape[0] - 1)
        left = csr_matrix(np.ones([rewrite_arr.shape[0] - 1, 1]))
        addition = hstack((left, idty))
        temp = addition.dot(rewrite_arr)
        sumofrow = temp.multiply(temp).sum(1)
        if sumofrow.all() == False:
          #endtime = time.time()
          #print (endtime - starttime)
	  return True
        data = csr_matrix(vstack((data, temp)))	
        datasize += temp.shape[0] 
      data = data[1:]
      datasize -= 1
    #endtime = time.time()
    #print (endtime - starttime)
    return False
