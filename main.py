"""
redis cluster 初始化, 扩容, 缩容

全局默认:
    1. 端口默认为 6379

初始化:
    1. redis-trib 1.1.1.1 2.2.2.2
    2. 默认 6379 端口

扩容:
    1. redis-trib -c 1.1.1.1 -a 3.3.3.3 4.4.4.4

缩容:
    1. redis-trib -c 1.1.1.1 -d 3.3.3.3 4.4.4.4
"""
import fire


class RedisCLuster(object):

    def create(self, *nodes):
        print(nodes)


if __name__ == '__main__':
    # calculator = Calculator()
    fire.Fire(RedisCLuster)
