class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        for i in range(len(flowerbed) - 1, -1, -1):
            if len(flowerbed) == 1:
                if flowerbed[0] == 0:
                    count += 1
                break

            if (i == 0) and (flowerbed[(i)] == 0) and (flowerbed[(i+1)] == 0):
                flowerbed[i] = 1
                count += 1

            elif (i < (len(flowerbed)-1)) and (flowerbed[(i-1)] == 0) and (flowerbed[i] == 0) and (flowerbed[(i+1)] == 0):
                flowerbed[i] = 1
                count += 1
            
            elif (flowerbed[(i)] == 0) and (flowerbed[i-1] == 0) and (i == (len(flowerbed)-1)):
                flowerbed[i] = 1
                count += 1

        
        if count >= n:
            return True
        else:
            return False
                    