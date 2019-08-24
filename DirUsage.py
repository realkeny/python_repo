import os, sys
from os.path import join, getsize
#rootDir = "C:\\Scripts"
def getfoldersizes(rootDir):
    dir_size = [(dir,sum([getsize(join(dir,file)) for file in fileList])) for dir, subdir, fileList in os.walk(rootDir)]
    sorted_dir_size = sorted(dir_size, key = lambda x:x[1], reverse = True)
    return sorted_dir_size


def gettopdir(dirpath, num):
    dir_list = getfoldersizes(dirpath)
    return dir_list[:num]
        

def print_header(msg,border):
    header_border = border * len(msg)
    print(header_border)
    print(msg)
    print(header_border + "\n")
    print("Directory name" + "\tSize")


def printout(list_object):
    print_header("Directory listing by size", "=")
    for x,y in list_object:
        print('{} \t{}'.format(x,y))


def main():
    if len(sys.argv) >= 2:
       dir_size = getfoldersizes(sys.argv[1])
       printout(dir_size)



if __name__ == "__main__":
    main()
