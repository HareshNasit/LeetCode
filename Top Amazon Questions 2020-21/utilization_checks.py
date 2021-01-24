import math

def finalInstances(instances, averageUtil):
    """
    :type instances: int
    :type averageUtil: List[int]
    :rtype: int
    """
    upper_limit = 2 * (10**8)
    # print(upper_limit)
    index = 0
    for util in averageUtil:
        if index > len(averageUtil) - 1:
            break
        if averageUtil[index] > 1 and averageUtil[index] < 25:
            if instances > 1:
                instances = math.ceil(instances / 2.0)
                index += 10
        elif averageUtil[index] > 60:
            if instances * 2 <= upper_limit:
                print(instances * 2 < upper_limit)
                instances *= 2
                index += 10
        # print('index',index)
        # print('instances', instances)
        index += 1
    return instances

print(finalInstances(100000000, [30,95,4,8,19,89]))
