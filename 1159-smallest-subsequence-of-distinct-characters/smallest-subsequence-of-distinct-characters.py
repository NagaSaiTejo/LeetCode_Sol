class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {}
        for i in range(len(s)):
            last_occurrence[s[i]] = i
        stack = []
        seen = set()
        for i in range(len(s)):
            char = s[i]
            if char in seen:
                continue
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return "".join(stack)