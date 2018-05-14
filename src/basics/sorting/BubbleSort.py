'''
核心：冒泡，持续比较相邻元素，大的挪到后面，因此大的会逐步往后挪，故称之为冒泡。
'''
# 平均情况与最坏情况均为 O(n^2), 使用了 temp作为临时交换变量，空间复杂度为 O(1).

def bubbleSort(alist):
    for i in range(len(alist)):
        print(alist)
        for j in range(1, len(alist)-i):
            if alist[j-1] > alist[j]:
                alist[j-1],alist[j] = alist[j],alist[j-1]
    
    return alist

if __name__ == '__main__':
    unsorted_list = [6,5]
    print(bubbleSort(unsorted_list))