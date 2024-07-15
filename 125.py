s = "tab a cat"

r = len(s)-1
l = 0
result = True

while l < r:
    if s[l].isalnum() and s[r].isalnum():
        if s[l].lower() != s[r].lower():
            result = False
        r -= 1
        l += 1
    
    else:
        if s[l].isalnum():
            r -= 1

        else:
            l += 1
        
print(result)

