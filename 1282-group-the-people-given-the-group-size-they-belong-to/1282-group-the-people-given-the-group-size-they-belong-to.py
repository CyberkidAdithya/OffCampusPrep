class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        hp = collections.defaultdict(lambda:[])
        for i in range(len(groupSizes)):
            if len(hp[groupSizes[i]]) == groupSizes[i]:
                ans.append(hp[groupSizes[i]])
                hp[groupSizes[i]] = [i, ]
            else:
                hp[groupSizes[i]].append(i)
        for val in hp.values():
            ans.append(val)
        return ans