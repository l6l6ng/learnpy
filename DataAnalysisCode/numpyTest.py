#encoding=utf-8
import numpy as np

def main():
    lst = [[1,3,5],[2,4,6]]
    print(type(lst))

    np_list = np.array(lst,dtype=float)
    print(type(np_list))

    print(np_list.shape)

    print(np_list.dtype)

    print(np.zeros([2,4]))
    print(np.ones([2,4]))

    print(np.random.rand(2,4))
    print(np.random.randint(2,4,5))

if __name__ == "__main__":
    main()