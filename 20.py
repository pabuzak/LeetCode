class Solution(object):
    def isValid(self, s):
        stack = []

        if len(s) == 1:
            return False

        for n in range(len(s)):
            if s[n] not in "})]":
                stack.append(s[n])

            else:
                if stack == []:
                    return False
                    
                current = stack.pop()
                if (current != '[' and s[n] == ']') or (current != "{" and s[n] == "}") or (current != "(" and s[n] == ")"):
                    return False
        if stack != []:
            return False

        return True
        