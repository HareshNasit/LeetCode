def processLogFile(logs, threshold):
    """
    :type logs: List[str]
    :type threshold: int
    :rtype: List[str]
    """
    users = {}
    output_lst = []
    for log in logs:
        split_log = log.split(" ")
        if split_log[0] != split_log[1]:
            if split_log[0] not in users:
                users[split_log[0]] = 1
            else:
                users[split_log[0]] += 1

            if split_log[1] not in users:
                users[split_log[1]] = 1
            else:
                users[split_log[1]] += 1
        else:
            if split_log[0] not in users:
                users[split_log[0]] = 1
            else:
                users[split_log[0]] += 1

    for user in users:
        print(user)
        if users[user] >= threshold:
            output_lst.append(user)
    return output_lst



logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
threshold = 2
print(processLogFile(logs, threshold))
