import os
import sys
import time
from platform import python_implementation
# 计算函数运行时间的装饰器
def caculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("函数运行时间为：%s" % (end_time - start_time))
    return wrapper

def detect_python_interpreter():
    try:
        from platform import python_implementation
    except ImportError: # pragma: no cover
        def python_implementation():
            """Return a string identifying the Python implementation."""
            if 'PyPy' in sys.version:
                return 'PyPy'
            if os.name == 'java':
                return 'Jython'
            if sys.version.startswith('IronPython'):
                return 'IronPython'
            return 'CPython'
    return python_implementation()

