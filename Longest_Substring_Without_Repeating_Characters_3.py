class Solution(object):
    @staticmethod
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store the last positions of each character
        char_index = {}
        max_length = 0
        start = 0  # Start index of the current window

        for i in range(len(s)):
            # If the character is already in the dictionary and its index is within the current window
            if s[i] in char_index and char_index[s[i]] >= start:
                # Move the start to the next position after the repeated character
                start = char_index[s[i]] + 1

            # Update the last seen index of the character
            char_index[s[i]] = i

            # Update the maximum length found so far
            max_length = max(max_length, i - start + 1)

        return max_length
