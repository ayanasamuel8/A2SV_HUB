# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        array = [_ for _ in range(n)]
        queue = deque(array)
        index = 0
        while queue:
            front = queue.popleft()
            if queue:
                queue.append(queue.popleft())
            array[front] = deck[index]
            index += 1
        return array
