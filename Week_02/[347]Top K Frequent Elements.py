# Given a non-empty array of integers, return the k most frequent elements. 
# 
#  Example 1: 
# 
#  
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: nums = [1], k = 1
# Output: [1] 
#  
# 
#  Note: 
# 
#  
#  You may assume k is always valid, 1 ≤ k ≤ number of unique elements. 
#  Your algorithm's time complexity must be better than O(n log n), where n is t
# he array's size. 
#  It's guaranteed that the answer is unique, in other words the set of the top 
# k frequent elements is unique. 
#  You can return the answer in any order. 
#  
#  Related Topics 堆 哈希表 
#  👍 568 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        frequency = defaultdict(int)
        for i in nums: frequency[i] += 1

        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        for key, value in frequency.items():
            bucket[value].append(key)

        res = []
        for i in range(n, -1, -1):
            res.extend(bucket[i])
            if len(res) == k: return res
# leetcode submit region end(Prohibit modification and deletion)
