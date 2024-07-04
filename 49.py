strs = ["eat","tea","tan","ate","nat","bat"]
group_anagram = []

for n in range(len(strs)):
    anagram = set()

    for i in range(len(strs)):
        if i != n:
            if sorted(strs[n]) == sorted(strs[i]):
                anagram.add(strs[n])
                anagram.add(strs[i])

    
    if anagram:
        if anagram not in group_anagram:
            group_anagram.append(anagram)

for n in range(len(group_anagram)):
    group_anagram[n] = list(group_anagram[n])


for i in range(len(strs)):
    anagram = set()
    count = 0
    for n in range(len(group_anagram)):
        if strs[i] not in group_anagram[n]:
            count += 1

    if count == len(group_anagram):
        anagram.add(strs[i])
        group_anagram.append(list(anagram))


print(group_anagram)
        
