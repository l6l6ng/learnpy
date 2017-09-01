#encoding=utf-8
import numpy as np
def startMain():
    lst = [[1,3,5],[2,4,6]]
    print type(lst)

    np_lst = np.array(lst)
    print type(np_lst)
    np_lst = np.array(lst,dtype=np.float)
    print type(np_lst)
    print np_lst.shape
    print np_lst.dtype
    print np_lst.itemsize
    print np_lst.size

    print np.ones([3,4])

    print np.random.randint(2,5)

if __name__=="__main__":
    startMain()