import heapq
def fillTheTruck(num: int, boxes: List[int], unitSize: int, unitsPerBox: List[int], truckSize: int) -> int:
    if num < 1 or len(boxes) < 1 or unitSize < 1 or len(unitsPerBox) < 1 or truckSize < 1:
        return 0

    heap = []
    for i in range(num):
        box = boxes[i]
        while box > 0:
            heapq.heappush(heap, -1 * unitsPerBox[i])
            box -= 1
    res = 0
    while truckSize > 0:
        if len(heap) > 0:
            res += -1 * heapq.heappop(heap)
        truckSize -= 1
    return res
