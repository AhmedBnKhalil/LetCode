from Longest_Substring_Without_Repeating_Characters_3 import Solution


def test_lengthOfLongestSubstring():
    assert Solution.lengthOfLongestSubstring("dvdf") == (3)


def test_lengthOfLongestSubstring2():
    assert Solution.lengthOfLongestSubstring("abcabcbb") == 3


def test_lengthOfLongestSubstring3():
    assert Solution.lengthOfLongestSubstring("bbbbb") == (1)


def test_lengthOfLongestSubstring4():
    assert Solution.lengthOfLongestSubstring("pwwkew") == (3)
