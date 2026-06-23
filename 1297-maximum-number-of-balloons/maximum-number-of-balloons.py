class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts={'b':0,'a':0,'l':0, 'o':0, 'n':0}
        for char in text:
            if char in counts:
                counts[char] += 1
        balloons_formed=0
        while True:
            if (counts['b'] >= 1 and 
                counts['a'] >= 1 and 
                counts['l'] >= 2 and 
                counts['o'] >= 2 and 
                counts['n'] >= 1):

                counts['b'] -= 1
                counts['a'] -= 1
                counts['l'] -= 2
                counts['o'] -= 2
                counts['n'] -= 1
                balloons_formed += 1
            else:
                break
        return balloons_formed 