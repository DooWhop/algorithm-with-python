'''
Created on 2018年5月11日

list作为最基本的python数据结构之一， 可以很轻松的实现stack。 
如果需要更高效的stack， 建议使用deque。
'''

stack = []
len(stack) # size of stack

# more efficient stack
import collections
stack = collections.deque()
