# 实验一:循环和递归实现二分查找：	（python）
# 递归：
def binarySort(lst, value):
    min = 0
    max = len(lst) - 1
    if min > max:
        return -1
    mid = (min + max) // 2
    if lst[mid] == value:
        return value
    elif lst[mid] > value:
        return binarySort(lst[:mid], value)
    elif lst[mid] < value:
        return binarySort(lst[mid + 1:], value)


lst = [3, 8, 2, 5, 9, 11, 4]
lst = sorted(lst)
print(binarySort(lst, 9))
