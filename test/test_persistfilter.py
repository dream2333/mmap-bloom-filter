from multiprocessing import Process
from threading import Thread
import time
from core.persistfilter import PersistFilter
from tools import caculate_time

# 本地过滤器容量10亿 中添加100万元素 单次19hash 最差情况写入760k 

# 单进程
# 随机 读+写 67秒 二次运行 34秒
# 顺序 读+写 72秒 二次运行 35秒

# 6进程 
# 随机 读+写 21秒 二次运行 6秒
# 顺序 读+写 23秒 二次运行 6.85秒

# 32进程 
# 随机 读+写 20-26秒 二次运行 6.24秒
# 顺序 读+写 16-20秒 二次运行 6.05秒

# 服务器四进程 1.1w/s


# 测试在百亿容量中连续添加一万个元素所需的时间
def test_add():

    # 设置容量十亿，误判率百万分之一
    persist_filter = PersistFilter("/home/dream/桌面/testfilter.bin", 1000000000,0.000001)
    for i in range(100000):
        persist_filter.add(f"{i}")
    persist_filter.close()
    assert 1

# 测试在百亿容量中查找一万个是否存在所需的时间
def test_exist():
    # 设置容量十亿，误判率百万分之一
    dup_count = 0
    persist_filter = PersistFilter("/home/dream/桌面/testfilter.bin", 1000000000,0.000001)
    for i in range(1000000):
        if f"{i}" in persist_filter:
            dup_count+=1
    print(dup_count)
    assert 1

# 多线程添加
def test_multi_t_add():
    persist_filter = PersistFilter("/home/dream/桌面/testfilter.bin", 1000000000,0.000001)
    def multi_test(start,end):
        print(start,end)
        time.sleep(2)
        for i in range(start,end):
            persist_filter.add(f"{i}")
    
    def run(times,t_count):
        thread_list = []
        for i in range(t_count): 
            step = int(times/t_count)
            p = Thread(target= multi_test,args=(i*step,i*step+step))
            p.start()
            thread_list.append(p)

        for i in thread_list:
            p.join()
        persist_filter.close()
    run(100000,8)
    # 设置容量百亿，误判率百万分之一

# 多进程添加
def test_multi_p_add():
    def multi_test(start,end):
        print(start,end)
        persist_filter = PersistFilter("/home/dream/桌面/testfilter.bin", 1000000000,0.000001)
        time.sleep(2)
        for i in range(start,end):
            persist_filter.add(f"{i}")
        persist_filter.close()
    
    def run(times,t_count):
        process_list = []
        for i in range(t_count): 
            step = int(times/t_count)
            p = Process(target= multi_test,args=(i*step,i*step+step))
            p.start()
            process_list.append(p)

        for i in process_list:
            p.join()
    run(1000000,8)
    # 设置容量百亿，误判率百万分之一

# 多进程获取
def test_multi_p_exist():
    def multi_test(start,end):
        persist_filter = PersistFilter("/home/dream/桌面/testfilter.bin", 1000000000,0.000001)
        time.sleep(2)
        for i in range(start,end):
            f"{i}" in persist_filter
        persist_filter.close()
    
    def run(times,t_count):
        process_list = []
        step = int(times/t_count)
        for i in range(t_count): 
            p = Process(target= multi_test,args=(i*step,i*step+step))
            p.start()
            process_list.append(p)

        for i in process_list:
            p.join()
    run(1000000,6)
    # 设置容量百亿，误判率百万分之一