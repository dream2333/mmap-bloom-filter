import math
import time
from collections import namedtuple
import mmh3
import struct
import mmap


# 计算函数运行时间的装饰器
def caculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("函数运行时间为：%s" % (end_time - start_time))

    return wrapper


@caculate_time
def create_file(file_path, size):
    """
    # 快速生成大文件
    :param file_path: 文件路径
    :param size: 文件大小，本函数以GB为单位，也可以根据需求设置为KB或MB等
    :return:
    """
    lfile = open(file_path, "wb")
    # 偏移文件写入位置；位置减掉一个字节
    lfile.seek(1024 * 1024 * 1024 * size - 1)
    # 写入0x00
    lfile.write(b"\x00")
    lfile.close()


# 过滤器
class BloomFilter(object):
    def __init__(self, num, error_rate):
        """
        :param num: 预计插入的元素个数
        :param error_rate: 允许的误判率
        :return: 字节数组大小和哈希函数个数
        """
        # 计算位数组大小
        bit_array_size = int(-(num * math.log(error_rate)) / (math.log(2) ** 2))
        # 计算哈希函数个数
        hash_function_num = int((bit_array_size / num) * math.log(2))
        # 计算字节数
        cost_bytes = math.ceil(bit_array_size / 8)
        # self.bit_array_size = bit_array_size
        # self.hash_function_num = hash_function_num
        # self.bit_array = [0] * bit_array_size
        return cost_bytes, bit_array_size, hash_function_num

    def add(self, value):
        """
        :param value: 待插入的元素
        """
        # 计算哈希值
        hash_value_list = self.get_hash_value(value)
        for hash_value in hash_value_list:
            # 将对应的bit位置为1
            self.bit_array[hash_value] = 1

    def is_contain(self, value):
        """
        :param value: 待查找的元素
        :return: True or False
        """
        # 计算哈希值
        hash_value_list = self.get_hash_value(value)
        for hash_value in hash_value_list:
            # 如果有一个bit位为0，说明不存在
            if self.bit_array[hash_value] == 0:
                return False
        return True

    def get_hash_value(self, value):
        """
        :param value: 待计算哈希值的元素
        :return: 哈希值列表
        """
        for i in range(self.hash_function_num):
            # 计算哈希值
            hash_value = mmh3.hash64(value, i, signed=False)
            # 取模，映射到虚拟内存中
            yield hash_value % self.bit_array_size


if __name__ == "__main__":
    cost_bytes, bit_array_size, hash_function_num = caculate_filter_info(100000000000, 0.00001)
    a = mmh3.hash64("123", signed=False)
    print(a)
