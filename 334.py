nums = [1,1,-2,6]

triplet = False
first = float("inf")
second = float("inf")

for n in nums:
    if n < first:
        first = n

    elif n < second and n != first:
        second = n

    elif n > second:
        triplet = True
    

print(triplet)