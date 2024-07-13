candies = [2, 3, 5, 1, 3]
extraCandies = 3

output = [False] * len(candies)
max_candy = max(candies)

for n in range(len(candies)-1, -1, -1):
    if (candies[n] + extraCandies) >= max_candy:
        output[n] = True

print(output)