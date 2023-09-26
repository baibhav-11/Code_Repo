class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Initialize a stack to keep track of characters
        stack = []
        # Initialize a dictionary to keep track of character frequencies
        char_count = {}
        
        # Count the frequency of each character in the string
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Initialize a set to keep track of characters in the stack
        stack_set = set()
        
        for char in s:
            # Decrement the frequency of the character
            char_count[char] -= 1
            
            if char in stack_set:
                continue
            
            # While the current character is smaller than the character at the top of the    stack,
            # and there are more occurrences of the character later in the string,
            # pop characters from the stack and remove them from the stack_set
            while stack and char < stack[-1] and char_count[stack[-1]] > 0:
                popped_char = stack.pop()
                stack_set.remove(popped_char)
            
            # Add the current character to the stack and stack_set
            stack.append(char)
            stack_set.add(char)
        
        # Convert the stack to a string and return
        return ''.join(stack)
