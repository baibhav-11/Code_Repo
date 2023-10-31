class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        rankings = {}

        for i, s in enumerate(sorted_scores):
            if i == 0:
                rankings[s] = "Gold Medal"
            elif i == 1:
                rankings[s] = "Silver Medal"
            elif i == 2:
                rankings[s] = "Bronze Medal"
            else:
                rankings[s] = str(i + 1)

        answer = [rankings[score[i]] for i in range(len(score))]
        return answer
