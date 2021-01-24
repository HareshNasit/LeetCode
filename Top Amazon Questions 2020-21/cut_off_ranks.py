def countLevelUpPlayers(cutOffRank, num, scores):
    if cutOffRank <= 0:
        return 0

    frequencies = [0 for i in range(100 + 1)]
    for score in scores:
        frequencies[score] += 1

    ans = 0
    current_rank = 1
    for i in range(100, -1, -1):
        if frequencies[i] == 0:
            continue
        ans += frequencies[i]
        current_rank += frequencies[i]
        if current_rank > cutOffRank:
            break
    return ans

print(countLevelUpPlayers(3, 4, [100,50,50,25]))
