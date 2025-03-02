
def bs(num, t, index):
    lhs = 0
    rhs = len(num)-1
    mid = len(num)//2

    if len(num) <= 1 and num[0] != t:
        return -1

    elif num[mid] > t:
        return bs(num[:mid], t, index)

    elif num[mid] < t:
        index += mid
        return bs(num[mid:], t, index)

    else:
        return index+mid


## index, plus index by mid
nums = [-1,0,2,4,6,8]
target = 4




print(bs(nums, target, index=0))