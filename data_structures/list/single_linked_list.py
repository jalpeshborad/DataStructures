# coding: utf-8
# -*- coding: utf-8 -*-

__author__ = "Jalpesh Borad"
__email__ = "jalpeshborad@gmail.com"


from data_structures.list.node import Node


class SingleLinkedList(object):
    def __init__(self):
        self._head = Node()
        self._tail = self._head

    @property
    def _count(self):
        _c = 0
        _temp = self._head
        while _temp:
            _c += 1
            print(_temp)
            _temp = _temp.next
        return _c

    def __str__(self):
        _str = "["
        _temp = self._head
        while _temp:
            if _temp.data:
                _str += f"{_temp.data}, "
            _temp = _temp.next
        _str = _str.rstrip(", ")
        return f"{_str}]"

    def _add_init_data(self):
        pass

    def _add_node_at_beginning(self, value):
        _temp_node = Node(value)
        _temp_node.next = self._head
        self._head = _temp_node

    def _add_node_at_the_end(self, value):
        _new_node = Node(value)
        self._tail.next = _new_node
        self._tail = _new_node

    def _add_node_at_position(self, position, value):
        _index = 1
        _temp_node = self._head
        while _index <= position:
            if _index == position:
                _new_node = Node(value)
                _new_node.next = _temp_node.next
                _temp_node.next = _new_node
            _index += 1
            _temp_node = _temp_node.next

    def append(self, value):
        self._add_node_at_the_end(value)

    def __setitem__(self, position, value):
        if position == 0:
            self._add_node_at_beginning(value)
        elif position == self._count:
            self._add_node_at_the_end(value)
        elif 0 < position < self._count:
            self._add_node_at_position(position, value)
        else:
            raise IndexError("Out of Index")

    def __getitem__(self, position):
        print(self._count)
        if position >= self._count:
            raise IndexError("Out of Index")

        _index = 0
        _temp_node = self._head
        while True:
            if _index == position:
                return _temp_node.data
            _temp_node = _temp_node.next
            _index += 1

    def __len__(self):
        return self._count


if __name__ == '__main__':
    s_list = SingleLinkedList()
    print(s_list)
    for _i in range(5):
        s_list[_i] = 1 + _i * 2
        print(s_list)
    print(s_list)
    s_list.append("Haha")
    print(s_list)
    s_list[3] = "Mutation"
    print(s_list)
    print(s_list[7])
