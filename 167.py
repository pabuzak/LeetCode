numbers=[-5,-3,0,2,4,6,8]
target=5

l = 0
r = len(numbers)-1

while l < r:
    num1 = numbers[l]
    num2 = numbers[r]

    if num1 + num2 == target:
        print([l+1, r+1])
        break
            
    else:
        if r-1 == l and l != len(numbers)-1:
            r = len(numbers)-1
            l += 1
        else:
            r-=1
    