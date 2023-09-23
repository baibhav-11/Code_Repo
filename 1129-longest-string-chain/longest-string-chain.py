class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort the words by length
        words.sort(key=len)
        
        # Initialize a dictionary to store the length of the longest chain ending at each word
        word_chain_lengths = {}
        
        # Initialize the maximum chain length to 1 (single-word chain)
        max_chain_length = 1
        
        for word in words:
            # Initialize the length of the chain for this word as 1
            word_chain_lengths[word] = 1
            
            # Try removing each character from the word and check if it exists in the dictionary
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                if prev_word in word_chain_lengths:
                    # Update the chain length for the current word
                    word_chain_lengths[word] = max(word_chain_lengths[word], word_chain_lengths[prev_word] + 1)
            
            # Update the maximum chain length if needed
            max_chain_length = max(max_chain_length, word_chain_lengths[word])
        
        return max_chain_length

        