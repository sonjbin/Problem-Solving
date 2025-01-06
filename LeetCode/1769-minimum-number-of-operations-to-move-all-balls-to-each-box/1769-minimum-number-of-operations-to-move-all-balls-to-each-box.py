class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [int(i) for i in boxes]
        n = len(boxes)
        ball_moves = [0] * n

        # left to right
        moves = 0
        cnt = 0
        for i in range(n):
            ball_moves[i] += moves
            cnt += boxes[i]
            moves += cnt

        # right to left
        moves = 0
        cnt = 0
        for i in range(n-1, -1, -1):
            ball_moves[i] += moves
            cnt += boxes[i]
            moves += cnt
 

        return ball_moves

