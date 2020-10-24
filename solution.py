with open('input.txt', encoding='utf-8') as f:
    lst = []
    N = int(f.readline())
    for line in f:
        man = line.strip().split()
        # print(man)
        man = list(map(int, man[-3:]))
        if man[0] >= 40 and man[1] >= 40 and man[2] >= 40:
            sm = sum(man)
            man.append(sm)
            lst.append(tuple(man))
            # print(lst)

lst.sort(key=lambda p: -p[3])
# print(*lst, sep='\n')

score = 0
cnt = 1
passing_score_tenderer = lst[0][3]
passing_score = None

if len(lst) <= N:
    output = 0
else:
    for i in range(1, len(lst)):
        if lst[i][3] == lst[i - 1][3]:
            cnt += 1
        else:
            score += cnt
            if score > N:
                output = passing_score
                break
            cnt = 1
            passing_score = passing_score_tenderer
            passing_score_tenderer = lst[i][3]
    else:
        output = 1

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(str(output))
