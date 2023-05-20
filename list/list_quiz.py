Arr = [[0,1], [0,0], [4,5]]
answer = 0
for i in Arr:
    for j in i:
        if j == 0:
            answer += 1
print(answer)

