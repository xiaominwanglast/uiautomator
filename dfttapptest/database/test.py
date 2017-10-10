#coding:utf-8
from multiprocessing import Pool
class addd():
    @classmethod
    def add(self,num):
        print num
if __name__ == "__main__":
    pool = Pool(3)
    a_obj = addd()
    for i in range(10):
        pool.apply_async(a_obj.add,args=(i,))
    pool.close()
    pool.join()


