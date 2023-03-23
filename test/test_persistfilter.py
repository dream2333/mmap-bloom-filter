from core.persistfilter import PersistFilter
from tools import caculate_time


@caculate_time
def test_add():
    # 设置容量百亿，误判率百万分之一
    persist_filter = PersistFilter("G:/testfilter.bin", 10000000000,0.000001)
    for i in range(1000):
        persist_filter.add(f"{i}")
    persist_filter.close()
    assert 1

@caculate_time
def test_find_exist():
    # 设置容量百亿，误判率百万分之一
    dup_count = 0
    persist_filter = PersistFilter("G:/testfilter.bin", 10000000000,0.000001)
    for i in range(10000):
        if f"{i}" in persist_filter:
            dup_count+=1
    print(dup_count)
    assert 1

