# coding: utf-8
# -*- coding: utf-8 -*-

__author__ = "Jalpesh Borad"
__email__ = "jalpeshborad@gmail.com"

"""
A collection/list of data with constraint 
that insertion or removal can be performed from only one end that is called top of the stack
Also known as Last In First Out (LIFO)

All the operation on the stack takes constant time i.e has time complexity of O(1)
"""


class Stack(object):
    def __init__(self):
        self._items = []

    def is_empty(self):
        """
        Returns True if stack is empty else returns False
        :return: Bool
        """
        return False if self._items else True

    def count(self):
        """
        Returns # of elements in the stack
        :return: int
        """
        return len(self._items)

    def push(self, value):
        """
        Adds element on top of the stack
        :param value: can be any object
        :return: None
        """
        self._items.append(value)

    def pop(self):
        """
        Pops top element from the stack and returns the same
        :return: Top element of the stack
        """
        return self._items.pop()

    def top_element(self):
        """
        Returns top most element of the stack
        :return:
        """
        return self._items[-1]
