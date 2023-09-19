class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i, row in enumerate(image):
            image[i] = row[::-1]
            for j in range(len(row)):
                 image[i][j] = int(not image[i][j])
        return image
