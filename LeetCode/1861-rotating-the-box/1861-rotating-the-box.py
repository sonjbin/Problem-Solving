class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        output = [["." for _ in range(m)] for _ in range(n)]
        box = box[::-1]
        stone = "#"
        obstacle = "*"
        empty = "."
        
        for i in range(m):
            stone_cnt = 0
            last_obstacle = n
            for j in range(n-1, -1, -1):
                if box[i][j] == stone:
                    stone_cnt += 1
                if box[i][j] == obstacle:
                    output[j][i] = obstacle
                # faced obstacle or top of the box
                if box[i][j] == obstacle or j == 0:
                    # shift all found stone to bottom
                    for s in range(stone_cnt):
                        output[last_obstacle-1-s][i] = stone
                    last_obstacle = j
                    stone_cnt = 0

        return output
