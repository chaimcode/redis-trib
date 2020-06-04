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
import sys
import argparse
import inspect
from enum import Enum
from functools import singledispatch, wraps


def dispatcher(func):
    __dispatcher = singledispatch(func)

    @wraps(func)
    def wrapper(*args, **kw):
        return __dispatcher.dispatch(args[1].__class__)(*args, **kw)

    wrapper.register = __dispatcher.register
    return wrapper


class RedisCLusterCreate(object):

    def __init__(self, *nodes):
        self.create(*nodes)

    def create(self, *nodes):
        """ create redis cluster
        """
        print(nodes)


class RedisCLusterExtend(object):
    def __init__(self, exist_random_node, *add_nodes):
        self.execute(exist_random_node, *add_nodes)

    def extend(self, exist_random_node, *add_nodes):
        """ extend redis cluster
        """
        print(exist_random_node, add_nodes)


class RedisCLusterShrink(object):
    def __init__(self, exist_random_node, *delete_nodes):
        self.shrink(exist_random_node, *delete_nodes)

    def shrin(self, exist_random_node, *delete_nodes):
        """ shrin redis cluster
        """
        print(exist_random_node, delete_nodes)


class RedisCLusterActionDispatcher(object):
    @dispatcher
    def dispatch(self, action, *args, **kwargs):
        cls_name = self.get_cls_name(action)
        cls_ = self.get_cls(cls_name)
        cls_(*args, **kwargs)

    def get_cls(self, cls_name):
        cls_ = getattr(sys.modules[__name__], cls_name)
        return cls_

    def get_cls_name(self, action):
        return f'RedisCLuster{action.title()}'


class StrEnum(Enum):

    @staticmethod
    def is_private(k):
        return str(k).startswith('__')

    @classmethod
    def to_list(cls):
        members = []
        for k, v in inspect.getmembers(cls):
            if cls.is_private(k):
                continue
            members.append(str(v))
        return members

    @classmethod
    def to_string(cls):
        return ', '.join(cls.to_list())

    def __str__(self):
        return self.value

    __repr__ = __str__


class ActionEnum(StrEnum):
    create = 'create'
    extend = 'extend'
    shrink = 'shrink'


def useage():
    parser = argparse.ArgumentParser(description='redis-trib for redis cluster.')

    parser.add_argument('action', help=f'action, eg: {ActionEnum.to_string()}', choices=ActionEnum.to_list())
    parser.add_argument('nodes', help='redis node address', nargs='+')
    parser.add_argument('-c', '--cluster', help='existed redis cluster address')
    parser.add_argument('-a', '--add', help='add a new redis node')
    parser.add_argument('-d', '--delete', help='delete a redis node')

    return parser


def main():
    parser = useage()

    # parser.print_help()

    args = parser.parse_args()
    # print(args)
    # print(args.nodes)

    action = args.action
    nodes = args.nodes
    cluster = args.cluster
    add_node = args.add
    del_node = args.delete

    dispatcher = RedisCLusterActionDispatcher()
    dispatcher.dispatch(action, *nodes)


if __name__ == '__main__':
    main()
