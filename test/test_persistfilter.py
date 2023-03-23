from core.persistfilter import PersistFilter
from tools import caculate_time


# 测试在百亿容量中连续添加一万个元素所需的时间
def test_add():
    # 设置容量百亿，误判率百万分之一
    persist_filter = PersistFilter("F:/testfilter.bin", 10000000000,0.000001)
    for i in range(100000):
        persist_filter.add(f"{i}")
    persist_filter.close()
    assert 1

# 测试在百亿容量中查找一万个是否存在所需的时间
def test_exist():
    # 设置容量百亿，误判率百万分之一
    dup_count = 0
    persist_filter = PersistFilter("F:/testfilter.bin", 10000000000,0.000001)
    for i in range(100000):
        if f"{i}" in persist_filter:
            dup_count+=1
    print(dup_count)
    assert 1

