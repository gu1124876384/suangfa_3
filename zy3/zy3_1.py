# 给n个数中找出最小k个数

# 类似于快排的思想，不同的地方在于每趟只需要往一个方向走
# 按照从小到大的顺序，寻找前K个最小值
def qselect(ary_list, k):
    if len(ary_list) < k:
        return ary_list

    tmp = ary_list[0]
    left = [x for x in ary_list[1:] if x <= tmp] + [tmp]
    llen = len(left)
    if llen == k:
        return left
    if llen > k:
        return qselect(left, k)
    else:
        right = [x for x in ary_list[1:] if x > tmp]
        return left + qselect(right, k-llen)
    pass
lst = [3, 8, 2, 5, 9, 11, 4]
lst = sorted(lst)
print(qselect(lst, 3))