# n = int(input())
# villages = list(map(int, input().split()))
# m = int(input())
# shelters = list(map(int, input().split()))

villages = []
shelters = []
nearest = [None] * 5
print(nearest)
# n = int(input())
# dist_v = list(map(int, input().split()))
# for i in range(n):
#     villages.append((i + 1, dist_v[i]))
# villages.sort(key=lambda item: item[1])
# m = int(input())
# dist_s = list(map(int, input().split()))
# for i in range(m):
#     shelters.append((i + 1, dist_s[i]))
# shelters.sort(key=lambda item: item[1])

# print(villages, shelters)

n = 5
villages = [(4, 8), (3, 13), (10, 17), (8, 20), (6, 29)]
m = 3
shelters = [(2, 19), (3, 20), (6, 39)]

k = -1
for village in villages:
    mn = 1000000001
    for i in range(k, m):
        distance = abs(shelters[i][1] - village[1])
        if distance < mn:
            mn = distance
            k += 1
        else:
            k -= 1


# print(villages, shelters)
