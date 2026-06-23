class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_counts = {}
        for char in text:
            char_counts[char] = char_counts.get(char, 0) + 1
            
        b_count = char_counts.get('b', 0)
        a_count = char_counts.get('a', 0)
        l_count = char_counts.get('l', 0) // 2 
        o_count = char_counts.get('o', 0) // 2
        n_count = char_counts.get('n', 0)
        
        return min(b_count, a_count, l_count, o_count, n_count)