
# 
# Your previous Plain Text content is preserved below:
# 
# Consider the following triangle:
# 
# 3
# 7 1
# 9 4 6
# 2 1 9 3
# 
# A "valid" path through this triangle goes from top to bottom via adjacent cells (down, or down and to the right). 
# 
# Among all the valid paths through the triangle there is one path which produces the largest path sum: That is, 3 + 7 + 4 + 9 = 23.
# 
# Now consider the following triangle:
# 
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
# 
# Find the maximum path sum from top to bottom of this triangle.
# 
# NOTE: The above triangle is your only input. It is up to you to copy it into your solution and parse it into an appropriate data structure.


TRIANGLE_INPUT1 = """3
7 1
9 4 6
2 1 9 3"""

TRIANGLE_INPUT2 = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


# convert to 1D
splitWithNewline = TRIANGLE_INPUT1.split('\n')

# convert to 2D
triangle = []
for i in range(len(splitWithNewline)):
    triangle.append(splitWithNewline[i].split(' '))

# change str to int
for i in range(len(triangle)):
    for j in range(i+1):
        triangle[i][j] = int(triangle[i][j])

class Solution:
    def maximumTotal(self, triangle):
        for row in range(1, len(triangle)):
            for col in range(row+1):
                triangle[row][col] = int(triangle[row][col])
                if col == 0:
                    triangle[row][col] += triangle[row-1][col] 
                elif col == row:
                    triangle[row][col] += triangle[row-1][col-1]
                elif col< row:
                    triangle[row][col] += max(triangle[row-1][col-1], triangle[row-1][col])
        return max(triangle[-1])
s = Solution()
print(s.maximumTotal(triangle))