from multiprocessing import Process

from core.persistfilter import PersistFilter


def multi_test():
    persist_filter = PersistFilter("/home/dream/桌面/testfilter.bin", 1000000000,0.000001)
    for i in range(1000):
        persist_filter.add(f"{i}")
    persist_filter.close()
    
if __name__ == "__main__":
    process_list = []
    for i in range(5):  #开启5个子进程执行fun1函数
        p = Process(multi_test) #实例化进程对象
        p.start()
        process_list.append(p)

    for i in process_list:
        p.join()
