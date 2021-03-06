class NodePoint(object):
#链接表的节点 节点分数据区和地址区
#数据区存需要存的数据 地址区存下一节点的内存地址
    def __init__(self, element, next_=None):
        self.__elem = element
        self.next = next_  # next域的值需要按需修改 外部可以直接访问

    def get_elem(self):  # 由于将元素域的变量设为了私有变量 不希望在类外对其直接调用并修改 所以添加了get方法 无set方法
        return self.__elem



class LinkedList(object):
#链表 一种常见的基础数据结构 为一种线性表 但不会按线性的顺序存储数据 而是靠每个节点存储下一节点的指针
#在python里通过使用变量名无数据类型的特性 和python解释器的垃圾回收机制 可以很简单得实现链表
#以及使用链表来实现堆栈的特性
    def __init__(self, head=None):  # 初始化链表首项默认为空如果创建时未传入参数
        self.__head = head
        if head is None:
            self.__size = 0
        else:
            self.__size = 1

    def __str__(self):
        str_all = ""
        p = self.__head
        while p:
            str_all += "%d " % p.get_elem()
            p = p.next
        return str_all

    def is_empty(self):  # 判断链表是否为空
        return self.__head is None

    def size(self):  # 读取链表长度
        return self.__size

    def prepend(self, elem):  # 在链表首部添加元素
        self.__head = NodePoint(elem, self.__head)
        self.__size += 1

    def append(self, elem):  # 在链表尾部添加元素
        note_item = NodePoint(elem)
        if self.is_empty():
            self.__head = note_item
        elif self.__head.next is None:
            self.__head.next = note_item
        else:
            p = self.__head  # p是为了while循环设置的过渡变量
            while p.next:
                p = p.next
            p.next = note_item
        self.__size += 1

    def insert(self, index, elem):  # 在制定位置添加元素
        """
        :param index: start from 0
        :param elem:
        :return:
        """
        if index <= 0:
            self.prepend(elem)
        elif index > self.size() - 1:
            self.append(elem)
        else:
            p = self.__head
            while index - 1 > 0:
                index -= 1
                p = p.next
            note_item = NodePoint(elem, p.next)
            p.next = note_item
        self.__size += 1

    def pop(self):  # 从链表尾部pop元素
        p = self.__head
        if p is None:
            return None
        elif p.next is None:  # 只有一个元素的时候
            element = p.get_elem()
            self.__head = None
            self.__size -= 1
            return element
        else:
            while p.next.next:
                p = p.next
            element = p.next.get_elem()
            p.next = None
            self.__size -= 1
            return element

    def pop_head(self):  # 从链表头部pop元素
        if self.is_empty():
            return None
        else:
            element = self.__head.get_elem()
            self.__head = self.__head.next
            self.__size -= 1
            return element

    def search(self, pred):  # 根据给定的搜索条件谓语来搜索元素
        p = self.__head
        if p:
            while p:
                if pred(p.get_elem()):  # pred为自定义的方法 用来判断元素是否符合条件
                    yield p.get_elem()
                p = p.next
