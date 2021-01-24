def fetch_items_to_display(items, sortParameter, sortOrder, itemsPerPage, pageNumber):
    if sortParameter == 0:
        if sortOrder == 1:
            items.sort(key=lambda x: x[0], reverse=True)
        else:
            items.sort(key=lambda x: x[0])
    elif sortParameter == 1:
        if sortOrder == 1:
            items.sort(key=lambda x: x[1], reverse=True)
        else:
            items.sort(key=lambda x: x[1])
    elif sortParameter == 2:
        if sortOrder == 1:
            items.sort(key=lambda x: x[2], reverse=True)
        else:
            items.sort(key=lambda x: x[2])

    return_lst = []
    for i in range(pageNumber * itemsPerPage, (pageNumber+1) * itemsPerPage):
        if i < len(items):
            return_lst.append(items[i][0])
        else:
            break
    return return_lst
    #           (OR)
    # itemIndStart = (pageNumber * itemsPerPage)
    # itemIndEnd = (pageNumber+1) * itemsPerPage
    #
    # items = (item[0] for i, item in enumerate(sorted(items, key=lambda x: x[sortParameter],reverse=sortOrder)) if itemIndStart <= i < itemIndEnd)
    # return [item for item in items]




print(fetch_items_to_display([["item1", 10,15], ["item2",3,4], ["item3", 17, 8]], 1, 0, 2, 0))
