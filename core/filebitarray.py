import math
import mmap
import sys


class FileBitArray:
    __slots__ = "__f", "__m"

    def __init__(self, filename, bit_array_size):
        """
        将大文件映射到虚拟内存并提供bitarray接口
        :param filename: 文件名
        :param bit_array_size: 位数组大小
        """
        size = math.ceil(bit_array_size / 8)
        # 创建指定大小空文件
        try:
            self.__createfile(filename,size)
        except:
            ...
        self.__f = open(filename, "r+b",buffering=0)
        self.__m = mmap.mmap(self.__f.fileno(), size, access=mmap.ACCESS_DEFAULT)
        # 如果系统位linux，则通知内核随机读写优化
        if sys.version_info >= (3, 8) and sys.platform != "win32":
            self.__m.madvise(mmap.MADV_RANDOM)


    def __createfile(self,filename,size):
        with open(filename,'xb') as f:
            f.seek(size-1)
            f.write(b'\x00')
            
    # 对文件对象内存映射进行读bit操作
    def __getitem__(self, index):
        byte_offset, bit_offset = divmod(index, 8)
        byte = self.__m[byte_offset]
        bit = (byte >> (7 - bit_offset)) & 1
        return bit

    # 对文件对象内存映射进行写bit操作
    def __setitem__(self, index, value):
        byte_offset = index // 8
        bit_offset = index % 8
        byte = self.__m[byte_offset]
        if value:
            byte |= 1 << 7 - bit_offset
        else:
            byte &= ~(1 << 7 - bit_offset)
        self.__m[byte_offset] = byte
        # 刷盘
        # flush_offset = byte_offset // mmap.ALLOCATIONGRANULARITY * mmap.ALLOCATIONGRANULARITY
        # self.__m.flush(flush_offset,byte_offset-flush_offset+1)

    # 同步刷全盘
    def flush(self):
        self.__m.flush()

    def __len__(self):
        return self.__m.size()

    def close(self):
        self.__m.close()
        self.__f.close()
