#!/bin/env python


class dicto(dict):
    def __init__(self, *args, **kwargs):
        super(dicto, self).__init__(*args, **kwargs)
        self.__dict__ = self

    def export(self):
        """exports all attributes to a true dict"""
        d = dict()
        for k, v in self.items():
            d[k] = v
        return d
