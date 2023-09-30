"""
You created a game that is more popular than Angry Birds.
Each round, players receive a score between 0 and 100, which you use to rank them from highest to lowest. So far you're using an algorithm that sorts in O(n*lg n) time, but players are complaining that their rankings aren't updated fast enough. You need a faster sorting algorithm.

Write a function that takes a list of unsorted_scores and the highest_possible_score in the game, and returns a sorted list of scores in less than O(n*lg n) time.

Time: O(n)
Space: O(n)
"""


def sort_scores(scores: list[int], max_score: int) -> list[int]:
    result = [0] * len(scores)
    score_counts = [0] * (max_score + 1)
    for s in scores:
        score_counts[s] += 1
    i = len(scores) - 1
    for s in range(max_score + 1):
        for _ in range(score_counts[s]):
            result[i] = s
            i -= 1
    return result


cases = (
    ([37, 89, 41, 65, 91, 53], 100, [91, 89, 65, 53, 41, 37]),
    ([1, 1, 1], 100, [1, 1, 1]),
    ([0, 100, 50], 100, [100, 50, 0]),
)
for scores, max_score, want in cases:
    got = sort_scores(scores, max_score)
    assert got == want, f"got: {got}, want: {want} ({scores} {max_score})"
