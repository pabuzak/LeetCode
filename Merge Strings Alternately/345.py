s = "leetcode"

vowels = "aeiouAEIOU"
reverse = ""
count = 0
string = ""

for i in range(len(s) - 1, -1, -1):
    if s[i] in vowels:
        reverse += s[i]


for i in range(len(s)):
    if s[i] in vowels:
        string += reverse[count]
        count += 1
    else:
        string += s[i]

print(string)