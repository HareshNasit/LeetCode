def fiveStartReviews(productRatings, ratingsThreshold):
    count = 0
    tempList = productRatings.copy()

    while(getRating(tempList) < ratingsThreshold / 100):
        distinctList = []
        for productRating in tempList:
            distinct = ((productRating[0] + 1) / (productRating[1] + 1)
                        ) - ((productRating[0]) / (productRating[1]))
            distinctList.append(distinct)

        index = distinctList.index(max(distinctList))
        tempList[index][0] = tempList[index][0] + 1
        tempList[index][1] = tempList[index][1] + 1
        count = count + 1

    return count


def getRating(productRatings):
    sum = 0
    for i in productRatings:
        sum = i[0]/i[1] + sum

    return sum / len(productRatings)
