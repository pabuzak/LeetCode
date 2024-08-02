nums=[0,-1]


result = 0
seq = set(nums)
num = 0

for n in seq:
    if n-1 in seq:
        print(n)


print(result)