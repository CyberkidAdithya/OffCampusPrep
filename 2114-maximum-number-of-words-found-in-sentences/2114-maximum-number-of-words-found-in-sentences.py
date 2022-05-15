class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxx = 0
        for line in sentences:
            count = 0
            for word in line:
                if word == " ":
                    count += 1
            if count > maxx:
                maxx = count
        return maxx + 1