class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """


st = 'abb'
st = list(st)
st_reverse=st.copy()
st_reverse.reverse()
print(st, '\n', st_reverse)
new_list = []
for i in range(len(st)):
    if st[i] != st_reverse[i]:
        continue

    if st[i] == st_reverse[i]:
        print('palindrome', st[i], st_reverse[i])
        new_list.append(st[i])

    if st[i] == st[i+1]:

        new_list.append(st[i+1])

if len(new_list) == 0:
    new_list.append(st[0])
delimiter = ""
join_str = delimiter.join(new_list)
print(join_str)
