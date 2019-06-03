from operator import methodcaller, itemgetter, attrgetter
import random, math


def test_attrgetter():
    # 属性获取
    pi = attrgetter("pi")
    print(pi(math))


def test_methodcaller():
    # 方法调用器,获取对象的方法进行调用  instance.run(args) ==> methodcaller("run", args)(instance)
    method1 = methodcaller("randint", 1, 10)
    print(method1(random))


def test_itemgetter():
    # 元素获取
    data = (23, 123, 3, 12, 3, 1)
    print(itemgetter(0)(data))  # 获取数组或元组的对应下标的数
    data = [(1, 2), (2, 3), (4, 4), (3, 1)]
    data.sort(key=itemgetter(0))  # 根据元组的第一个下标的值进行排序
    print(data)

