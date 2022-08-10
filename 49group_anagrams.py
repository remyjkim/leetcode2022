#Runtime: 109 ms, faster than 90.16% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.8 MB, less than 59.18% of Python3 online submissions for Group Anagrams.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        hashmap = defaultdict(list)
        for string in strs:
            print(f'string is {string}')
            hashmap["".join(sorted(string))].append(string)
        return hashmap.values()