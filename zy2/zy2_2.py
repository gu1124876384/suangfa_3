def merge(lfrom, lto, low, mid, high):
    i, j, k = low, mid, low
    while i < mid and j < high:  # 记录两段段首记录中较小的
        if lfrom[i] <= lfrom[j]:
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1
    while i < mid:  # 复制第一段记录
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:  # 复制第二段记录
        lto[k] = lfrom[j]
        j += 1
        k += 1


def merge_pass(lfrom, lto, llen, slen):
    i = 0
    while i + 2 * slen < llen:  # 归并长slen的两段
        merge(lfrom, lto, i, i + slen, i + 2 * slen)
        i += 2 * slen
    if i + slen < llen:  # 剩下两段，后段长度小于slen
        merge(lfrom, lto, i, i + slen, llen)
    else:  # 只剩下一段，复制到表lto
        for j in range(i, llen):
            lto[j] = lfrom[j]


def merge_sort(lst):
    slen, llen = 1, len(lst)
    templst = [None] * llen
    while slen < llen:
        merge_pass(lst, templst, llen, slen)
        slen *= 2
        merge_pass(templst, lst, llen, slen)  # 结果存回原位
        slen *= 2
    print
    lst, templst

lst = [3, 8, 2, 5, 9, 11, 4]
lst = sorted(lst)