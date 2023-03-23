from tools import detect_python_interpreter

if detect_python_interpreter() == "PyPy":
    from core.murmurhash import hash128 as hash128_x64
else:
    from mmr3 import hash128_x64
    


def test_murmurhash_bench():
    # 一百万次hash取值
    for i in range(1000000):
        hash = hash128_x64(f"{i}", seed=31)

def test_get_offset_range():
    for i in range(5000000):
        for seed in range(19):
            # 计算哈希值
            hash128 = hash128_x64("1231242341235345", seed)

