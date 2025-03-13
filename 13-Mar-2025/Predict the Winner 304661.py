# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        queue = deque(nums)
        def recursion(path, result, index):
            if not path:
                result[index] = 0
                return result

            front = path.popleft()
            from_left = recursion(path,[0,0],1-index)
            from_left[index] += front
            path.appendleft(front)

            back = path.pop()
            from_right = recursion(path,[0,0], 1-index)
            from_right[index] += back
            path.append(back)
            if from_right[index] > from_left[index]:
                return from_right
            elif from_right[index] < from_left[index]:
                return from_left
            elif from_right[1-index] < from_left[1-index]:
                return from_right
            else:
                return from_left
        res = recursion(queue,[0,0],0)
        return res[0] >= res[1]
