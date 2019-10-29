import os
import sys


def parse_file(path):
    
    fd = open(path)
    i = 0
    spaces = 0
    tabs = 0
    for i,line in enumerate(fd):
        spaces += line.count(' ')
        tabs += line.count('\t')
    fd.close()

    return (spaces, tabs, i + 1)
path = '//home//student//2017//8390//Desktop//test.txt'


print(path)
if os.path.exists(path):
    print("a")
    print(parse_file(path))
