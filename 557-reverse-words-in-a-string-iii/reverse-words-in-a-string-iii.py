class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the sentence into words
        words = s.split()
        
        # Reverse each word and join them back together with space
        reversed_words = [word[::-1] for word in words]
        result = ' '.join(reversed_words)
        
        return result