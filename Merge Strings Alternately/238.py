import math
nums = [1, 2, 3, 4]

products = []


for n in range(len(nums)):
    product1 = 1
    product2 = 1
    num = nums[n+1:]

    product1 = math.prod(num)

    num = nums[:n]
    product2 = math.prod(num)

    products.append(product1 * product2)
    

print(products)


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