Arr = [12, 44, 5, 88, 2, 55, 3, 2, 31, 23, 4,5,3,2,1]
for i in range(len(Arr)):
    Min = i
    for j in range(i+1, len(Arr)):
        if Arr[Min] > Arr[j]:
            Min = j
    Arr[i],Arr[Min] = Arr[Min],Arr[i]
print(Arr[-1])