"""
redis cluster 初始化, 扩容, 缩容

全局默认:
    1. 端口默认为 6379

初始化:
    1. redis-trib create 1.1.1.1 2.2.2.2
    2. 默认 6379 端口

扩容:
    1. redis-trib extend -c 1.1.1.1 -a 3.3.3.3 4.4.4.4

缩容:
    1. redis-trib shrink -c 1.1.1.1 -d 3.3.3.3 4.4.4.4
"""
import fire


class RedisCLuster(object):

    def create(self, *nodes):
        """ create redis cluster
        """
        print(nodes)

    def extend(self, exist_random_node, *add_nodes):
        """ extend redis cluster
        """
        print(exist_random_node, add_nodes)

    def shrin(self, exist_random_node, *delete_nodes):
        """ shrin redis cluster
        """
        print(exist_random_node, delete_nodes)


if __name__ == '__main__':
    # calculator = Calculator()
    fire.Fire(RedisCLuster)
