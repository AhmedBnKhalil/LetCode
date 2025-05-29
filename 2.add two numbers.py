"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


l1 = [2, 4, 3]
l2 = [5, 6, 4]
l1.reverse()
l2.reverse()
print(l1, l2)
l1 = int(''.join(map(str, l1)))
l2 = int(''.join(map(str, l2)))

print(l1, type(l1))
print(l2, type(l2))
print(l1 + l2)

l3 = list(map(int, str(l1 + l2)))
l3.reverse()
print(l3)

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        var = l1.reverse
        var = l2.reverse
        l1 = int("".join(map(str, l1)))
        l2 = int("".join(map(str, l2)))
        l3 = list(map(int, str(l1 + l2)))
        l3.reverse()
        print(l3)


mn = Solution()
mn.addTwoNumbers([2, 4, 3], [5, 6, 4])
mn.addTwoNumbers([0], [0])
mn.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])
