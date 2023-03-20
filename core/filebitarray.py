import math
import mmap


class FileBitArray:
    __slots__ = "__f", "__m", "op"

    # 创建文件对象内存映射
    def __init__(self, filename, bit_array_size, sync_flush=False):
        size = math.ceil(bit_array_size / 8)
        try:
            open(filename, "xb").close()
        except:
            ...
        self.__f = open(filename, "r+b", buffering=1 if sync_flush else 0)
        self.__m = mmap.mmap(self.__f.fileno(), size, access=mmap.ACCESS_DEFAULT)
        # 写操作计数
        self.op = 0

    # 对文件对象内存映射进行读bit操作
    def __getitem__(self, index):
        byte_offset, bit_offset = divmod(index, 8)
        byte = self.__m[byte_offset]
        bit = (byte >> (7 - bit_offset)) & 1
        return bit

    # 对文件对象内存映射进行写bit操作
    def __setitem__(self, index, value):
        byte_offset, bit_offset = divmod(index, 8)
        byte = self.__m[byte_offset]
        if value:
            byte |= 1 << 7 - bit_offset
        else:
            byte &= ~(1 << 7 - bit_offset)
        self.__m[byte_offset] = byte

    # 同步刷盘
    def flush(self):
        self.__m.flush()

    def __len__(self):
        return len(self.__m) * 8

    def close(self):
        self.__m.close()
        self.__f.close()

