# 实验一:循环和递归实现二分查找：	（python）
# 循环：
def binarySort(lst, value):
    min = 0
    # max不减去1的话可能会导致索引超范围，比如最后可能min=max=len(lst)
    max = len(lst) - 1
    while min <= max:
        mid = (min + max)//2
        if lst[mid] == value:
            return value
        elif lst[mid] < value:
            min = mid + 1
        elif lst[mid] > value:
            max = mid - 1
    # value不存在，返回-1
    return -1



lst = [3,8,2,5,9,11,4]
lst = sorted(lst)
print(binarySort(lst, 9))
