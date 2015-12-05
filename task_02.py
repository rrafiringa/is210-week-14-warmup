#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Week 14 Task 02 """

from data import FRUIT


def get_cost_per_item(shoplist):
    """
    Args:
        shoplist (dict):  Shopping list
    Returns:
        dict: Fruit total cost per item keyed by fruits
    Examples:
        >>> get_cost_per_item({'Black Plum': 8,
                               'Bosc Pear': 4})

    """
    return {key: numfruits * FRUIT[key] for key,
            numfruits in shoplist.iteritems()}


if __name__ == '__main__':
    LIST = {'Black Plum': 8,
            'Bosc Pear': 4}
    print get_cost_per_item(LIST)