import time
from filebitarray import FileBitArray
from virtualmem import caculate_time


# 测试filebitarray的写入速度
@caculate_time
def test_write_sync():
    fba = FileBitArray("test", 100000000, sync_flush=True)
    for i in range(100000000):
        fba[i] = 1
        # if i % 1000000 == 0:
        #     fba.flush()
    fba.close()
    return 1