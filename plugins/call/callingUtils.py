from plugins.management.management import valid_group
import os
import sys
import file



class Member:
    def __init__(self,line):
        content = line.split()
        self.name = content.pop(0)
        self.id = content.pop(0)
        self.job = content
    def __str__(self):
        pass
    def __repr__(self):
        pass
