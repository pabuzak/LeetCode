# use hashmap, how many has that count of letters.

strs = ["eat","tea","tan","ate","nat","bat"]
res = {} # mapping charCount to list of Anagrams
output = []

alphabet = "abcdefghijklmnopqrstuvwxyz"

for s in strs:
    count = [0] * 26

    for letter in s:
        index_letter = alphabet.index(letter)
        count[index_letter] += 1
    
    if str(count) not in res:
        res[str(count)] = [s]

    else:
        res[str(count)].append(s)

for n in res.values():
    output.append(n)

print(output)






        
