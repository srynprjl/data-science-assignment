import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 4)

print("Heap after pushing values:", heap)

smallest = heapq.heappop(heap)
print("Smallest element removed:", smallest)

print("Heap after popping:", heap)
