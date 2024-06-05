class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        def fortnite(n):
            if n == "I":
                return 1
            elif n == "V":
                return 5
            elif n == "X":
                return 10
            elif n == "L":
                return 50
            elif n == "C":
                return 100
            elif n == "D":
                return 500
            elif n == "M":
                return 1000
 

        stack = []
        fortnite_resutl = 0
        for n in s:
            stack.append(n)

        while stack:
            current = stack.pop()

            if stack:
                next = stack[-1]
            else:
                next = None

            if (next == "I" and current == "V") or (next == "I" and current == "X"):
                result = fortnite(current) - fortnite(next)
                fortnite_resutl += result
                stack.pop()
            elif (next == "X" and current == "L") or (next == "X" and current == "C"):
                result = fortnite(current) - fortnite(next)
                fortnite_resutl += result
                stack.pop()
            elif (next == "C" and current == "D") or (next == "C" and current == "M"):
                result = fortnite(current) - fortnite(next)
                fortnite_resutl += result
                stack.pop()
            
            elif next == None:
                result = fortnite(current)
                fortnite_resutl += result

            else:
                result = fortnite(current)
                fortnite_resutl += result

        return fortnite_resutl
    
s = Solution()
print(s.romanToInt("MCDLXXVI"))