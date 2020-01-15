# 实验二：递归调运实现快速排序和合并排序（Python）
def quick_sort(lst):
    qsort_rec(lst, 0, len(lst) - 1)


def qsort_rec(lst, l, r):
    if l > r:
        return  # 分段无记录或只有一个记录
    i = l
    j = r
    pivot = lst[i]  # lst[i]是初始空位
    while i < j:
        while i < j and lst[j] >= pivot:  # 大记录，寻找比pivot大的元素
            j -= 1  # 向左扫描比pivot大的元素
        if i < j:  # lst[j] < pivot
            lst[i] = lst[j]
            i += 1  # 小于pivot的元素移到左边
        while i < j and lst[i] <= pivot:
            i += 1
        if i < j:  # lst[i] > pivot
            lst[j] = lst[i]
            j -= 1  # 大记录移到右边
        lst[i] = pivot  # 将pivot存入其最终位置
        qsort_rec(lst, l, i - 1)  # 递归处理左半区间
        qsort_rec(lst, i + 1, r)  # 递归处理右半区间

lst = [3, 8, 2, 5, 9, 11, 4]
lst = sorted(lst)
