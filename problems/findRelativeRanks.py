def findRelativeRanks(score):
    sorted_scores = sorted(score, reverse=True)
    rank_dict = {}

    for index, pontuation in enumerate(sorted_scores):
        if index == 0:
            rank_dict[pontuation] = "Gold Medal"
        elif index == 1:
            rank_dict[pontuation] = "Silver Medal"
        elif index == 2:
            rank_dict[pontuation] = "Bronze Medal"
        else:
            rank_dict[pontuation] = str(index + 1)

    result = []

    for pontuation in score:
        result.append(rank_dict[pontuation])

    return result