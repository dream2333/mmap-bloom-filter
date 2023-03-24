import io
import math

from core.filebitarray import FileBitArray
from tools import detect_python_interpreter
from core.primernumber import primer_numbers

# 如果是pypy,将使用自己的hash函数进行jit加速
if detect_python_interpreter() == "PyPy":
    from core.murmurhash import hash128 as hash128_x64
else:
    from mmr3 import hash128_x64


# 素数的英文是 a:
class PersistFilter(object):
    __slots__ = "bit_array_size", "hash_func_count", "bit_array", "primer_numbers"
    
    def __init__(self, filename: str, num: int, error_rate: float):
        """
        基于虚拟内存的持久化过滤器
        :param filename: 文件名
        :param num: 预计插入的元素个数
        :param error_rate: 允许的误判率
        :return: 字节数组大小和哈希函数个数
        """
        # 计算位数组大小
        self.bit_array_size = int(-(num * math.log(error_rate)) / (math.log(2) ** 2))
        # 计算哈希函数个数
        self.hash_func_count = int((self.bit_array_size / num) * math.log(2))
        self.primer_numbers = primer_numbers[0:self.hash_func_count]
        # 计算过滤器大小
        cost_bytes = math.ceil(self.bit_array_size / 8)
        cost_gigabytes = cost_bytes / 1024 / 1024 / 1024
        # 生成文件字节数组
        self.bit_array = FileBitArray(filename, self.bit_array_size)
        print(
            f"过滤器大小：{cost_gigabytes:.3f}GB "
            f"哈希函数个数：{self.hash_func_count} "
            f"误判率：{error_rate:1.8f} "
            f"预计插入元素个数：{num} "
        )

    def add(self, value: str):
        """
        将元素插入到过滤器中
        :param value: 待插入的元素
        """
        for index in self.get_offset_index(value):
            # 先读后写，将对应的bit位置为1
            if self.bit_array[index] == 0:
                self.bit_array[index] = 1
            # # 只写入
            # self.bit_array[index] = 1
            
    def __contains__(self, value: str):
        """
        判断元素是否存在于过滤器中
        :param value: 待查找的元素
        :return: True or False
        """
        # 对每个哈希值进行判断
        for index in self.get_offset_index(value):
            # 如果有一个bit位为0，说明不存在
            if self.bit_array[index] == 0:
                return False
        return True

    def get_offset_index(self, value: str):
        """
        根据hash函数的个数，计算不同hash在文件映射的bit位
        :param value: 待计算哈希值的元素
        :param hash_count: 哈希函数个数
        :return: 哈希值列表
        """
        # for seed in primer_numbers:
        #     # 计算哈希值
        #     hash128 = hash128_x64(value, seed)
        #     # 取模，映射到虚拟内存中的地址
        #     yield hash128 % self.bit_array_size
        # 使用生成式提高hdd性能
        offset_list =  [(hash128_x64(value, seed) % self.bit_array_size )for seed in primer_numbers]
        offset_list.sort()
        return offset_list

    def close(self):
        """
        关闭文件
        """
        self.bit_array.close()


if __name__ == "__main__":
    var = io.DEFAULT_BUFFER_SIZE
    print(var)
    PersistFilter("G:/testfilter.bin", 10000000000, 0.000001)
