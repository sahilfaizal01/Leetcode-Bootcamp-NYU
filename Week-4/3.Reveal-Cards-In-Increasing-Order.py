class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        index = collections.deque(range(N))
        res = [0] * N
        print('Deck:',sorted(deck))
        for card in sorted(deck):
            res[index.popleft()] = card
            if index:
                index.append(index.popleft())
        return res
        
