# Given two words (beginWord and endWord), and a dictionary's word list, find th
# e length of shortest transformation sequence from beginWord to endWord, such tha
# t: 
# 
#  
#  Only one letter can be changed at a time. 
#  Each transformed word must exist in the word list. 
#  
# 
#  Note: 
# 
#  
#  Return 0 if there is no such transformation sequence. 
#  All words have the same length. 
#  All words contain only lowercase alphabetic characters. 
#  You may assume no duplicates in the word list. 
#  You may assume beginWord and endWord are non-empty and are not the same. 
#  
# 
#  Example 1: 
# 
#  
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output: 5
# 
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog
# " -> "cog",
# return its length 5.
#  
# 
#  Example 2: 
# 
#  
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: 0
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible trans
# formation.
#  
# 
#  
#  
#  Related Topics 广度优先搜索 
#  👍 654 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hashset, res = set(wordList), 0
        leftDeq, rightDeq = deque([beginWord]), deque([endWord])
        leftVis, rightVis = {beginWord}, {endWord}
        if endWord not in hashset: return 0

        while leftDeq and rightDeq:
            res += 1
            if len(leftDeq) > len(rightDeq):
                leftDeq, rightDeq = rightDeq, leftDeq
                leftVis, rightVis = rightVis, leftVis

            for _ in range(len(leftDeq)):
                curWord = leftDeq.popleft()
                if curWord in rightVis: return res

                for i in range(len(beginWord)):
                    for j in range(26):
                        tmp = curWord[:i] + chr(ord('a') + j) + curWord[i+1:]
                        if tmp not in leftVis and tmp in hashset:
                            leftVis.add(tmp)
                            leftDeq.append(tmp)
        return 0
# leetcode submit region end(Prohibit modification and deletion)
