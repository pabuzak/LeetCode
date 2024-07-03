s = "rat"
t = "car"

s_list = list(s)

if len(t) > len(s):
    print(False)

for n in t:
    if n in s_list:
        i = s_list.index(n)
        s_list.pop(i)

if s_list == []:
    print(True)
else:
    print(False)


# faster way
# sorted_s = sorted(s)
# sorted_t = sorted(t)
# return sorted_s == sorted_t