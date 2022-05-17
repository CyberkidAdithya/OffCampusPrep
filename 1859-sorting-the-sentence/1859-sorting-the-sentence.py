class Solution:
    def sortSentence(self, s: str) -> str:
        arr = collections.defaultdict(lambda:"")
        words = s.split(' ')
        for i in range(len(words)):
            arr[int(words[i][-1]) - 1] = words[i][:-1]
        ans = []
        for i in range(len(arr.keys())):
            ans.append(arr[i])
        return " ".join(ans)
        