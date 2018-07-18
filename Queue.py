class Queue(object):
# queue 队列 为先进先出的线性表
# 这里用python的列表list来进行简单的入队和出队的实现
# 这里只实现了单向队列 后续会补充双向队列的实现
    def __init__(self):
        self.__que_list = []

    def enqueue(self, item):  # 入队操作 这里选择将list的尾部最为入队端 入队操作的时间复杂度为O(1)
        self.__que_list.append(item)

    def dequeue(self):  # 出队操作 这里与入队相对应 将list的首部作为出队端 出队的时间复杂度为O(n)
        return self.__que_list.pop(0)

    def size(self):  #返回队列的长度
        return len(self.__que_list)

    def is_empty(self):  #判断队列是否为空
        return self.__que_list is []
