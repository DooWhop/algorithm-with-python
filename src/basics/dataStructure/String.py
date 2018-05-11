'''
@author: liudp
'''

def printString():
    s1 = str()
    print(s1)
    # in python `''` or `""` is the same
    s2 = "shaunwei" # 'shaunwei'
    s2len = len(s2)
    print(s2len)
    # last 3 chars
    print(s2[-3:]) # wei
    print(s2[5:8]) # wei
    s3 = s2[:5] # shaun
    print(s3)
    s3 += 'wei' # return 'shaunwei'
    print(s3)
    # list in python is same as ArrayList in java
    s2list = list(s3)
    print(s2list)
    # string at index 4
    print(s2[4]) # 'n'
    # find index at first
    print(s2.index('w'))  # return 5, if not found, throw ValueError
    print(s2.find('w')) # return 5, if not found, return -1

if __name__ == '__main__':
    printString()