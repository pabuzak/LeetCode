nums = [1]
k = 1

element_dict = {}
output = []

temp = 0
temp_value = float('inf')

for n in nums:
    if n not in element_dict:
        element_dict[n] = 1

    else:
        element_dict[n] += 1

while k > 0:
    for value, key in element_dict.items():
        temp = max(temp, key)
        if temp == key:
            temp_value = value

    output.append(temp_value)
    element_dict[temp_value] = 0
    temp = 0
    k -= 1
