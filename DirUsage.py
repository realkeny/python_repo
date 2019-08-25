''' 
Script to display directory listing with sizes of each subdirectoies. it displays the sizes of the 
current directory if no argument is specified.
example: DirUsage.py C:\\Scripts 10
This sill displays the top 10 directories by sizes in C:\\Scripts.
Script written by Kehinde Adetutu (kenny.adetutu@gmail.com) August, 2019.
'''

import os, sys
from os.path import join, getsize

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


def formatSize(size):
    if size < 1024:
        conv_size = size
        return(str(conv_size) +' Bytes')
    if size >= 1024 and size < (1024**2):
        n = 1
        conv_size = round(size/(1024**n),1)
        return(str(conv_size) +' KB')
    elif size >= (1024**2) and size < (1024**3):
        n = 2
        conv_size = round(size/(1024**n),1)
        return(str(conv_size) +' MB')
    elif size >= (1024*3) and size < (1024**4):
        n = 3
        conv_size = round(size/(1024**n),1)
        return(str(conv_size) +' GB')
    elif size >= (1024*4) and size < (1024**5):
        n = 4
        conv_size = round(size/(1024**n),1)
        return(str(conv_size) +' TB')
    elif size >= (1024*5) and size < (1024**6):
        n = 5
        conv_size = round(size/(1024**n),1)
        return(str(conv_size) +' PB')
    else:
        n = 6
        conv_size = round(size/(1024**n),1)
        return(conv_size)



def printout(list_object):
    print_header("Directory listing by size", "=")
    for x,y in list_object:
        print('{} \t{}'.format(x,formatSize(y)))


def main():
    '''if no argument is passed to the script, use current folder'''
    if len(sys.argv) == 1:
        path = '.'
        dir_size = getfoldersizes(path)
        printout(dir_size)
    elif len(sys.argv) == 2:
        path = sys.argv[1]
        if os.path.exists(path):
            dir_size = getfoldersizes(path)
            printout(dir_size)
        else:
            print('Directory: '+ path +' does not exist.')
    elif len(sys.argv) == 3:
        path = sys.argv[1]
        num = sys.argv[2]
        try:
           n = int(num)
        except ValueError:
            print('Unable to covert to Int. second argument must be an integer')
        else:
            dir_size = gettopdir(path, n)
            printout(dir_size)
    else:
        ErrMsg = ''' 
            Invalid system arguments:
            Usage: DirUsage.py path num
            where path is the directory to check for size usage and num is the number
            of top directory to list.
        '''
        print(ErrMsg)


if __name__ == "__main__":
    main()
