
list = [ 5, 2, 6, 7, 10, -8, 0, 1]


def getIndex(pos):
    for i in range(0,len(list)):
        if(list[i] == pos):
            return i+1
    else:
        return -1



element = 10
result = getIndex(element)
print("found at : " , result)





