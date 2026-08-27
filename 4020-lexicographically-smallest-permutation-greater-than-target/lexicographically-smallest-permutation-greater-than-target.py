class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        for i in range(n - 1, -1, -1):
            prefix = target[:i]
            temp = list(s)
            possible = True
            for ch in prefix:
                if ch in temp:
                    temp.remove(ch)
                else:
                    possible = False
                    break
            if not possible:
                continue
            temp.sort()
            for ch in temp:
                if ch > target[i]:
                    temp.remove(ch)
                    return prefix + ch + "".join(temp)
        return ""
