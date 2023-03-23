from core.filebitarray import FileBitArray
from tools import caculate_time


def test_write_bench():
    fba = FileBitArray("/media/dream/软件/Programming/vsProject/PersistFilter/testtest", 10000000000)
    for i in range(10000000):
        fba[i] = 1
    fba.close()
    assert 1

# 测试读取所有的数组元素
def test_read_array_elements():
    fba = FileBitArray("/media/dream/软件/Programming/vsProject/PersistFilter/testtest", 10000000000)
    for i in range(10000000):
        bit = fba[i]
    fba.close()
    print(bit)
    assert 1