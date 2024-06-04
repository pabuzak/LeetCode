str1 = "ABCDEF"
str2 = "ABC"

min_str = min(len(str1), len(str2))
max_str = max(len(str1), len(str2))
temp = ""
larger_str = ""

for n in range(min_str):
    if min_str == len(str2):
        temp = temp + str2[n]
        if min_str % (n+1) == 0:
            ans = int(min_str / (n+1))
            if (temp * ans) == str2:
                if max_str % (n+1) == 0:
                    ans = int(max_str / (n+1))
                    if str1[:n+1] == temp and (str1[:n+1] * ans == str1):
                        larger_str = temp
    
    elif min_str == len(str1):
        temp = temp + str1[n]
        if min_str % (n+1) == 0:
            ans = int(min_str / (n+1))
            if (temp * ans) == str1:
                if max_str % (n+1) == 0:
                    if str1[:n+1] == temp:
                        larger_str = temp

print(larger_str)