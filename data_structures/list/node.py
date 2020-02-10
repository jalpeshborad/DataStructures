# coding: utf-8
# -*- coding: utf-8 -*-

__author__ = "Jalpesh Borad"
__email__ = "jalpeshborad@gmail.com"


class Node(object):
    def __init__(self, value=None):
        self.data = value
        self.next = None

    def __str__(self):
        return f"Node(data={self.data}, next={self.next})"
