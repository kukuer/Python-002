# -*- coding: utf-8 -*-
# @Author  : xh.w
# @File    : job.py

# 作业一：

# 容器序列：list tuple collections.deque
# 扁平序列：str
# 可变序列：list collections.deque
# 不可变序列：str tuple

# 作业二：
# 自定义一个 python 函数，实现 map() 函数的功能。

def def_map(func, seq):
    return [func(arg) for arg in seq]



# 作业三：
# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
import time

def timer(func):
    def run_time(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} function run time: {start_time - end_time}')
        return result
    return run_time


@timer
def test(times):
    time.sleep(times)


if __name__ == '__main__':
    test(1)