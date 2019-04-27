"""
Copy files with given extensions
from given directory and all of its subdirectories
to a given destination
"""
from os import walk
from shutil import copy


def getExt(str):
    return str.split('.')[-1]


def runMain(src, dst, ext):
    for path, dirs, files in walk(src):
        for file in files:
            if getExt(file) in ext:
                copy(path + '\\' + file, dst)


if __name__ == '__main__':
    runMain(input("Type in src\n"), input("Type in dst\n"), input("Type in exts\n").split(' '))
