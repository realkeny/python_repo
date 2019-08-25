
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

print(formatSize(2048))
