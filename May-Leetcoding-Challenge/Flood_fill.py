class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #Perform Depth First Search
        color = image[sr][sc]
        if color == newColor:
            return image
        self.depth_first_search(image, sr, sc, color, newColor)
        return image

    def depth_first_search(self, image, row, column, color, newColor):
        if image[row][column] == color:
            image[row][column] = newColor
            if row >= 1:
                 self.depth_first_search(image, row - 1, column, color, newColor)
            if row + 1 < len(image):
                 self.depth_first_search(image, row + 1, column,color, newColor)
            if column >= 1:
                 self.depth_first_search(image, row, column - 1, color,  newColor)
            if column + 1 < len(image[0]):
                 self.depth_first_search(image, row, column + 1,color, newColor)
