nums = [1, 2, 3, 4]

products = []

before = [1]
after = []

product1 = 1
for n in range(len(nums)):
    print(product1)
    product1 *= nums[n]
    before.append(product1)

product2 = 1
for n in range(len(nums)-1, -1, -1):
    product2 *= nums[n]
    after.append(product2)

after.reverse()
after.append(1)

for n in range(len(nums)):
    multiply = before[n] * after[n+1]
    products.append(multiply)

print(before)
print(after)
print(products)

# print(products)


### o(n^2)

# nums = [-1,1,0,-3,3]

# products = []

# for i in range(len(nums)):
#     num1 = nums[i+1:]
#     num2 = nums[:i]

#     product = 1

#     for n in num1:
#         product *= n
    
#     for n in num2:
#         product *= n
#     products.append(product)

# print(products)