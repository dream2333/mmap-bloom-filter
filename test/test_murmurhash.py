from tools import detect_python_interpreter
from tools import caculate_time


@caculate_time
def test_murmurhash_bench():
    if detect_python_interpreter() == "PyPy":
        from core.murmurhash import hash128 as hash128_x64
    else:
        from mmr3 import hash128_x64
    # 一百万次hash取值
    for i in range(10000000):
        hash = hash128_x64(f"{i}", seed=31)
