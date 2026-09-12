from linked_list import LinkedList
from queue import Queue


class QueueLL(Queue):

    def __init__(self):
        self.__list = LinkedList()

    def enqueue(self, value):
        self.__list.prepend(value)

    def dequeue(self):
        return self.__list.pop()

    def is_empty(self):
        return len(self.__list) == 0

    def peek(self):
        return self.__list[len(self.__list)-1]

    def size(self):
        return len(self.__list)
