class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        srcColor = image[sr][sc]
        m, n = len(image), len(image[0])
        def fill(x, y):
            if x < 0 or x >= m:
                return
            if y < 0 or y >= n:
                return
            if image[x][y] != srcColor:
                return
            if image[x][y] == newColor:
                return
            image[x][y] = newColor
            fill(x + 1, y)
            fill(x - 1, y)
            fill(x, y + 1)
            fill(x, y - 1)
        fill(sr, sc)
        return image