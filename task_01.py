#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Week14 - Task 01 """

from pet import Pet


class Dog(Pet):
    """
    Canine class quadruped
    Args:
    Attributes:
    Examples:
    >>> woof = Dog(has_shots=True, **{'birthyear': 2010,
                                      'weight': 25,
                                      'length': 100,
                                      'color': 'red',
                                      'owner': 'Jesse'})
        >>> woof.has_shots
        True
    >>> woof.age
        2
    >>> woof.coat
        brown
    """
    def __init__(self, has_shots=False, **kwargs):
        self.has_shots = has_shots
        Pet.__init__(self, **kwargs)


if __name__ == '__main__':
    WOOF = Dog(has_shots=True, **{'birthyear': 2010,
                                  'weight': 25,
                                  'length': 100,
                                  'color': 'red',
                                  'owner': 'Jesse'})
    print WOOF.has_shots
    print WOOF.age
    print WOOF.owner
    print WOOF.color
    print WOOF.length
    print WOOF.weight
