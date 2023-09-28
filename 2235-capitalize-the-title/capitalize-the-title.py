class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()  # Split the title into words
        capitalized_words = []

        for word in words:
            if len(word) <= 2:
                # If the word has 1 or 2 letters, convert to lowercase
                capitalized_words.append(word.lower())
            else:
                # Otherwise, capitalize the first letter and convert the rest to lowercase
                capitalized_words.append(word[0].upper() + word[1:].lower())

        return ' '.join(capitalized_words)  # Join the words back together with spaces
