#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 rzavalet <rzavalet@noemail.com>
#
# Distributed under terms of the MIT license.

"""
An implementation of a Hash using mod.
Please implement the requiered methods.
"""

from HashScheme import HashScheme
import hashlib


class ModHash(HashScheme):

    def __init__(self):
        """
        You have to decide what members to add to the class
        """
        self.__scheme_name = 'Modular_Hash'
        self.nodes = []

    def __get_hash(self, value):
        """
        Calculates an initial hash using md5.
        """
        return int(hashlib.md5(value.encode()).hexdigest(), 16) % self.get_size()

    def get_size(self):
        """
        Returns the number of available buckets or nodes.
        """
        return len(self.nodes)

    def get_name(self):
        return self.__scheme_name

    def dump(self):
        """
        Auxiliary method to print out information about the hash
        """
        for i in range(self.get_size()):
            print("Node: {0} hash: {1}".format(self.nodes[i], i + 1))

    def add_node(self, new_node):
        """
        Possibly just increment a counter of number of nodes. You may also
        need to update Store to react in certain way depending on the
        scheme_name.
        """
        self.nodes.append(new_node)
        return 0

    def remove_node(self, node):
        """
        Possibly just decrement a counter of number of nodes. You may also
        need to update Store to react in certain way depending on the
        scheme_name.
        """
        try:
            self.nodes.remove(node)
        except ValueError:
            return 1

        return 0

    def hash(self, value):
        """
        Convert value to a number representation and then obtain mod(number_of_nodes)
        """
        if len(self.nodes) == 0:
            return None

        return self.nodes[self.__get_hash(value)]
