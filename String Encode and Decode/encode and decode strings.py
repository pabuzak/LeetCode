class Solution:
    def __init__(self):
        self.s = ""
        self.sl = ""
        self.temp = 0
        self.l = []

    def encode(self, strs: List[str]) -> str:
        for n in strs:
            self.s += n + "|"

        return self.s

    def decode(self, s: str) -> List[str]:
        for n in range(len(s)):
            if s[n] == "|":
                self.sl += s[self.temp:n]
                self.temp = n+1
                self.l.append(self.sl)
                self.sl = ""
        
        return self.l