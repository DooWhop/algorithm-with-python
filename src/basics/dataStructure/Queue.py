
'''
Queue 和 Stack 在 Python 中都是有 list ,[] 实现的。 在python 
list是一个dynamic array, 可以通过append在list的尾部添加元素， 通过pop()在list的尾部弹出元素实现Stack的FILO， 如果是pop(0)则弹出头部的元素实现Queue的FIFO。

'''

def printQueue():
    queue = []  # same as list()
    size = len(queue)
    queue.append(1)
    queue.append(2)
    print(queue.pop(0)) # return 1
    print(queue[0]) # return 2 examine the first element
    
if __name__ == '__main__':
    printQueue()